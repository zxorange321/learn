# -*- coding: utf-8 -*-
#/usr/bin/python

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import warnings
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import GridSearchCV
from sklearn.decomposition import PCA

mpl.rcParams['font.sans-serif'] = [u'SimHei']
mpl.rcParams['axes.unicode_minus'] = False

warnings.filterwarnings('ignore', category=FutureWarning)
path = 'datas/iris.data'
data = pd.read_csv(path, header=None)

x = data[list(range(4))]
y = pd.Categorical(data[4]).codes

print ('总样本数量： %d; 特征属性数目： %d' % x.shape)

x_train1, x_test1, y_train1, y_test1 = train_test_split(x, y, train_size = 0.8, random_state=14)
x_train, x_test, y_train, y_test = x_train1, x_test1, y_train1, y_test1
print ('训练样本数量： %d; 训练样本数量： %d' % (x_train.shape[0], x_test.shape[0]))

## 数据标准化
## StandardScaler
## 或   数据归一化
## MinMaxScaler

ss = MinMaxScaler()
x_train = ss.fit_transform(x_train)
x_test  = ss.transform(x_test)

## 特征选择： 从已有的特征中选择影响目标最大的特征属性
## 常用方法： 分类： F统计量， 卡方系数，互信息
##            连续： 皮尔逊相关系数，F统计量，互信息

## SelectKBest(卡方系数)
ch2 = SelectKBest(chi2, k=3)  # k=3 表示特征数
x_train = ch2.fit_transform(x_train, y_train)
x_test = ch2.transform(x_test)

select_name_index = ch2.get_support(indices=True)
print (' 对类别判断影响最大的三个特征属性分别是:', ch2.get_support(indices=False))
print (select_name_index)

## 降维，对于数据而言，如果特征比较多的情况下，建模的过程中，模型可能会比较复杂，
## 这个时候我们考虑将多维或者（高维）映射到低维度的数据空间中去
## 常用的方法： PCA 主成分分析（无监督）， 
## LDA： 线性判别分析（有监督）使得各类之间的方差最小 ---- 人脸识别
pca = PCA(n_components=2) ## 超参数设置，需要自己调整
x_train = pca.fit_transform(x_train)
x_test = pca.transform(x_test)

# 模型设置
model = DecisionTreeClassifier(criterion='entropy', random_state=0)
model.fit(x_train, y_train)
y_test_hat = model.predict(x_test)

print ("准确率： %f" % model.score(x_test,y_test))

N = 100
x1_min = np.min((x_train.T[0].min(), x_test.T[0].min()))
x1_max = np.min((x_train.T[0].max(), x_test.T[0].max()))
x2_min = np.min((x_train.T[1].min(), x_test.T[1].min()))
x2_max = np.min((x_train.T[1].max(), x_test.T[1].max()))

t1 = np.linspace(x1_min, x1_max, N)
t2 = np.linspace(x2_min, x2_max, N)
x1, x2 = np.meshgrid(t1, t2) 
x_show = np.dstack((x1.flat, x2.flat))[0]
y_show_hat = model.predict(x_show)
print (y_show_hat.shape)
y_show_hat = y_show_hat.reshape(x1.shape)


plt_light = mpl.colors.ListedColormap(['#A0FFA0', '#FFA0A0', '#A0A0FF'])
plt_dark = mpl.colors.ListedColormap(['r', 'g', 'b'])

plt.figure(facecolor='w')
plt.pcolormesh(x1, x2, y_show_hat, cmap=plt_light)
plt.scatter(x_test.T[0], x_test.T[1], c=y_test.ravel(), edgecolors='k', 
            s=150, zorder=10, cmap=plt_dark, marker='*') # 使用测试数据
plt.scatter(x_train.T[0], x_train.T[1], c=y_train.ravel(), edgecolors='k', 
            s=40, zorder=10, cmap=plt_dark) # 使用训练数据
plt.xlabel('特征属性1', fontsize=15)
plt.ylabel('特征属性2', fontsize=15)
plt.xlim(x1_min, x1_max)
plt.ylim(x2_min, x2_max)
plt.grid(True)
plt.title('燕尾花数据决策树分类分析', fontsize=18)
plt.show()

##--------------------------------------------------------

pipe = Pipeline([
        ('mms', MinMaxScaler()),
        ('skb', SelectKBest(chi2)),
        ('pca', PCA()),
        ('decision', DecisionTreeClassifier(random_state=0))
        ])
## GridSerachCV
## 1. 建立合适的机器学习模型
## 2. 对于当前的模型，设置一系列的模型超参数
## 3. 放入GridSearchCV 函数中， 对比所有设置的超参数，让函数选择最优（得分最高）的一组参数

parameters = {
        'skb__k':[1,2,3,4],
        'pca__n_components':[0.5, 0.99],
        'decision__criterion':['gini', 'entropy'],
        'decision__max_depth':[1,2,3,4,5,6,7,8,9,10],
        }
x_train2, x_test2, y_train2, y_test2 = x_train1, x_test1, y_train1, y_test1
gscv = GridSearchCV(pipe, param_grid=parameters, cv=3)
gscv.fit(x_train2, y_train2)
y_test_hat = gscv.predict(x_test2)
print ("最优参数列表", gscv.best_params_)
print ("score值", gscv.best_score_)
print ("gscv.score值", gscv.score(x_test2, y_test2))



##--------------------------------------------------------


mms_best = MinMaxScaler()
skb_best = SelectKBest(chi2, k=3)
pca_best = PCA(n_components=0.99)
decision_best = DecisionTreeClassifier(criterion='gini', max_depth=4)
x_train3, x_test3, y_train3, y_test3 = x_train1, x_test1, y_train1, y_test1
x_train3 = pca_best.fit_transform(skb_best.fit_transform(mms_best.fit_transform(x_train3), y_train3))
x_test3 = pca_best.transform(skb_best.transform(mms_best.transform(x_test3)))
decision_best.fit(x_train3, y_train3)

print(decision_best.score(x_test3, y_test3))



##--------------------------------------------------------




x_train4, x_test4, y_train4, y_test4 = train_test_split(x.iloc[:, :2], y, train_size=0.7, random_state=14)
depth = np.arange(1,15)
err_list = []
for d in depth:
    clf = DecisionTreeClassifier(criterion='entropy', max_depth=d)
    clf.fit(x_train4, y_train4)
    
    score = clf.score(x_test4, y_test4)
    error = 1-score
    err_list.append(error)
    print("%d深度，正确率%.5f" % (d, score))
    
    
plt.figure(facecolor='w')
plt.plot(depth, err_list, 'ro-', lw=3)
plt.xlabel('决策树深度', fontsize=16)
plt.ylabel('错误率', fontsize=16)
plt.grid(True)
plt.title('决策树深度太多，导致的过拟合问题', fontsize=18)
plt.show()

from skimage import io
from IPython.display import Image
import pydotplus
dot_data = tree.export_graphviz(model, out_file=None,
                               feature_names=['PCA1', 'PCA2'],
                               class_names=['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'],
                               filled=True,
                               rounded=True,
                               special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data)
Image(graph.create_png())


with open('iris.dot','w') as f:
    f = tree.export_graphviz(model, out_file=f)

import pydotplus
dot_data = tree.export_graphviz(model, out_file=None)
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_pdf('iris3.pdf')


