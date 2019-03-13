# hmmlearn框架说明

#hmmlearn中主要有两种模型，分布为：GaussianHMM和MultinomialHMM；
#如果观测值是连续的，那么建议使用GaussianHMM，否则使用MultinomialHMM；
#参数：初始的隐藏状态概率π参数为: startprob_；状态转移矩阵A参数为: transmat_; 
#状态和观测值之间的转移矩阵B参数为: emissionprob_(MultinomialHMM模型中)
#或者在GaussianHMM模型中直接给定均值(means)和方差/协方差矩阵(covars)。## MultinomialHMM案例
import numpy as np
import hmmlearn.hmm as hmm


# 定义变量
status = ['盒子1', '盒子2', '盒子3']
obs = ['白球', '黑球']
n_status = len(status)
m_obs = len(obs)
start_probability = np.array([0.2, 0.5, 0.3])
transition_probability = np.array([
    [0.5, 0.4, 0.1],
    [0.2, 0.2, 0.6],
    [0.2, 0.5, 0.3]
])

emission_probalitity = np.array([
    [0.4, 0.6],
    [0.8, 0.2],
    [0.5, 0.5]
])


# 定义模型
model = hmm.MultinomialHMM(n_components=n_status)
model.startprob_ = start_probability
model.transmat_ = transition_probability
model.emissionprob_ = emission_probalitity


# 运行viterbi预测的问题
se = np.array([[0, 1, 0, 0, 1]]).T
logprob, box_index = model.decode(se, algorithm='viterbi')
print("颜色:", end="")
print(" ".join(map(lambda t: obs[t], [0, 1, 0, 0, 1])))
print("盒子:", end="")
print(" ".join(map(lambda t: status[t], box_index)))
print("概率值:", end="")
print(np.exp(logprob)) # 这个是因为在hmmlearn底层将概率进行了对数化，防止出现乘积为0的情况# 使用MultinomialHMM进行参数的训练
import numpy as np
import hmmlearn.hmm as hmm


# 定义变量
states = ['盒子1', '盒子2', '盒子3']
obs = ['白球', '黑球']
n_states = len(states)
m_obs = len(obs)

model2 = hmm.MultinomialHMM(n_components=n_states, n_iter=20, tol=0.001)
X2 = np.array([
    [0, 1, 0, 0, 1],
    [0, 0, 0, 1, 1],
    [1, 1, 0, 1, 0],
    [0, 1, 0, 1, 1],
    [0, 0, 0, 1, 0]
])
model2.fit(X2)
print("输出根据数据训练出来的π")
print(model2.startprob_)
print("输出根据数据训练出来的A")
print(model2.transmat_)
print("输出根据数据训练出来的B")
print(model2.emissionprob_)

# 这时候的数据会变，是因为数据量太少，矩阵参数还没有收敛