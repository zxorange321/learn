# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

import sklearn as sk
# 训练集测试集划分
from sklearn.model_selection import train_test_split
# 数据标准化
from sklearn.preprocessing import StandardScaler
# 线性回归模型
from sklearn.linear_model import LinearRegression

path = './datas/ai_train1801.csv'
df = pd.read_csv(path, sep=',')
#print (df.head())
#print (df.describe())
#print (df.info())

x = df.drop(['血糖'], axis = 1, inplace=False)
y = df['血糖']
x_train, x_test, y_train, y_test = train_test_split(x,y, train_size=0.8, test_size=0.2)

ss = StandardScaler()
x_train = ss.fit_transform(x_train)
x_test  = ss.transform(x_test)

linear = LinearRegression()
linear.fit(x_train, y_train)
print ("训练集R^2:", linear.score(x_train, y_train))
print ("训练集R^2:", linear.score(x_test, y_test))

y_test_hat = linear.predict(x_test)
def mean_sequared_error(y_true, y_predict):
    mse = np.power(y_true-y_predict, 2).mean()
    return mse

print ("测试集mse", mean_sequared_error(y_test, y_test_hat))
name = list(x.columns)
print ("模型的系数:", list(zip(name, linear.coef_)))
print ("模型的斜率:", linear.intercept_)
