# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import  matplotlib.pyplot as plt
import pandas as pd



dataset = pd.read_csv("Data.csv")
X = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1]


from sklearn.preprocessing import Imputer


imputer = Imputer(missing_values= 'NaN', strategy= 'mean', axis = 0)
imputer.fit(X.iloc[:,1:3])

X.iloc[:,1:3] = imputer.transform(X.iloc[:,1:3])

# encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

labelencoder_X = LabelEncoder()
X.iloc[:, 0] = labelencoder_X.fit_transform(X.iloc[:,0])