# -*- coding: utf-8 -*-

import numpy as np
import tensorflow as tf
import sys
import random
import collections


### 1. 读取数据

content = ""
with open('./belling_the_cat.txt') as f:
    content = f.read()

words = content.split()
print (words)

def build_dataset(words):
    count = collections.Counter(words).most_common()
#    print ("count", count)

    ## 构建正向字典
    dictionary = dict()
    for word, _ in count:
        dictionary[word] = len(dictionary)

    ## 构建反向字典
    reverse_dictionary = dict(zip(dictionary.values(), dictionary.keys()))

    ## 函数值是返回正向字典和反向字典
    return dictionary,reverse_dictionary

dictionary, reverse_dictionary = build_dataset(words)
#print (dictionary)
#print (reverse_dictionary)

### 2. 开始构建模型参数
vocab_size = len(dictionary)
n_input = 3
n_hidden = 512
batch_size = 20

#with tf.variable_scope('scope1', reuse=True):
weight = tf.get_variable('weight_out', [2*n_hidden, vocab_size], \
                         initializer= tf.random_normal_initializer)
bias = tf.get_variable('bias_out', [vocab_size], \
                       initializer= tf.random_normal_initializer)


### 定义RNN
def RNN(x, weight, bias):
    x = tf.reshape(x, [-1, n_input])
    x = tf.split(x, n_input, 1)
    ## 调用tensorflow 接口来定义lstm_cell
    ## 构建前向cell
    rnn_cell_format = tf.nn.rnn_cell.BasicLSTMCell\
        (n_hidden, state_is_tuple=True, forget_bias=1.0)
    ## 构建后向cell
    rnn_cell_backmat = tf.nn.rnn_cell.BasicLSTMCell\
        (n_hidden, state_is_tuple=True, forget_bias=1.0)
    outputs, outputs_states_fw, output_states_hw = tf.nn.static_bidirectional_rnn\
        (rnn_cell_format, rnn_cell_backmat, x, dtype=tf.float32)
    return tf.matmul(outputs[-1], weight) + bias

### 数据转换
def build_data(offset):
    while offset + n_input > vocab_size:
        offset = random.randint(0, vocab_size-n_input)
        ## 随机产生样本范围中的3个连续的词，并将其中映射为数值
    symbols_in_key = [[dictionary[str(words[i])]] for i in range(offset, offset+n_input)]
    symbols_out_onehot = np.zeros([vocab_size], dtype=float)
    symbols_out_onehot[dictionary[str(words[offset+n_input])]] = 1.0
    return symbols_in_key, symbols_out_onehot

### 搭建损失函数
x = tf.placeholder(tf.float32, [None, n_input, 1])
y = tf.placeholder(tf.float32, [None, vocab_size])
pred = RNN(x, weight, bias)
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=pred, labels=y))
#with tf.variable_scope('scope2', reuse=True):
optimizer = tf.train.AdamOptimizer(learning_rate=1e-5).minimize(cost)

### 构造准确率计算函数
correct_pred = tf.equal(tf.argmax(pred, 1), tf.argmax(y,1))
### 把准确率变为百分比
accuary = tf.reduce_mean(tf.cast(correct_pred, tf.float32))


### 训练模型

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(50000):
        x_train, y_train = [], []
        for b in range(batch_size):
            new_x, new_y = build_data(random.randint(0, vocab_size))
            x_train.append(new_x)
            y_train.append(new_y)
        _opt = sess.run(optimizer, feed_dict={x:np.array(x_train), y:np.array(y_train)})
#        print ("train ... ")
        
        if i%100 == 0:
            acc, out_pred = sess.run([accuary, pred], feed_dict={x:np.array(x_train), y:np.array(y_train)})
            symbols_in = [reverse_dictionary[word_index[0]] for word_index in x_train[0]]
            symbols_out = reverse_dictionary[int(np.argmax(y_train, 1)[0])]
            pred_out = reverse_dictionary[int(np.argmax(out_pred,1)[1])]
            print ('epoch:%d, Acc:%f'%(i,acc))
            print ('%s-[%s]vs[%s]'%(symbols_in, symbols_out, pred_out))
            print (out_pred.shape)

    while True:
        start_sentence = input("Please input %s words:"%n_input)
        words = start_sentence.strip().split()
        if len(words) != n_input:
            continue
        elif words[0] == words[1] and words[1] == words[2] and words[2] == 'exit':
            break
        else: 
            pass
        
        print ("predicting ... ")
    
        try:
            symbols_in_keys = [dictionary[str(words[i])] for i in range(len(words))]
            for _ in range(1):
                keys = np.reshape(np.array(symbols_in_keys), [-1, n_input, 1])
                onehot_pred = sess.run(pred, feed_dict={x:keys})
                onehot_pred_index = int(tf.argmax(onehot_pred,1).eval())
                start_sentence = '%s%s'%(start_sentence, reverse_dictionary[onehot_pred_index])
                symbols_in_keys = symbols_in_keys[1:]
                symbols_in_keys.append(onehot_pred_index)
            print (start_sentence)
        except:
            print("Word not in dictionary")



