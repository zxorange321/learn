# -*- coding: utf-8 -*-

from sklearn.cross_validation import cross_val_score
from sklearn.datasets import make_blobs #生成聚类数据

# meta-estimator
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier 

from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis


classifiers = {
    'KN': KNeighborsClassifier(3),
    'SVC': SVC(kernel="linear", C=0.025),
    'SVC': SVC(gamma=2, C=1),
    'DT': DecisionTreeClassifier(max_depth=5),
    'RF': RandomForestClassifier(n_estimators=10, max_depth=5, max_features=1),  # clf.feature_importances_
    'ET': ExtraTreesClassifier(n_estimators=10, max_depth=None),  # clf.feature_importances_
    'AB': AdaBoostClassifier(n_estimators=100),
    'GB': GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0), # clf.feature_importances_
    'GNB': GaussianNB(),
    'LD': LinearDiscriminantAnalysis(),
    'QD': QuadraticDiscriminantAnalysis(),
    'LinearSVC':LinearSVC()
    }

    
    
X, y = make_blobs(n_samples=10000, n_features=10, centers=100, random_state=0)

import time

for name, clf in classifiers.items():
    start_time = time.time()
    scores = cross_val_score(clf, X, y)
    print(name,'\t--> ',scores.mean())
    end_time = time.time()
    print('程序用时：%f秒' % (end_time - start_time))
    
    