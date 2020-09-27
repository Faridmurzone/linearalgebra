#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 09:54:48 2020

@author: fmurzone
"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv('./tableexample.csv')
dataset.head(5)

dataset.shape

x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,1].values

X_train, X_test, Y_train, Y_test = train_test_split(x,y, test_size=0.2, random_state = 0)

print(X_train)

regressor = LinearRegression()
regressor.fit(X_train, Y_train)

viz_train = plt
viz_train.scatter(X_train, Y_train, color = 'blue')
viz_train.plot(X_train, regressor.predict(X_train), color = "black")
viz_train.title('Salario vs experiencia')
viz_train.xlabel("Experiencia")
viz_train.ylabel("Salario")
viz_train.show()

viz_train = plt
viz_train.scatter(X_test, Y_test, color = 'red')
viz_train.plot(X_test, regressor.predict(X_test), color = "black")
viz_train.title('Salario vs experiencia')
viz_train.xlabel("Experiencia")
viz_train.ylabel("Salario")
viz_train.show()

regressor.score(X_test, Y_test)
