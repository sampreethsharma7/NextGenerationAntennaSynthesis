# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 10:16:28 2022

@author: sinf5
"""
from keras.models import Sequential
from keras.layers import Dense
from sklearn.neighbors import KNeighborsRegressor 
from sklearn.linear_model import LinearRegression 
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
# Calling the function
X_train = pd.DataFrame()
Y_train = pd.DataFrame()
X_test = pd.DataFrame()
Y_test = pd.DataFrame()
X_train = pd.read_excel('C:/Users/sinf5/Desktop/Sampreeth/NewIdea-Attempt1/ML_DATA/Train-Input/TrainInput.xlsx')
Y_train = pd.read_excel('C:/Users/sinf5/Desktop/Sampreeth/NewIdea-Attempt1/ML_DATA/Train-Output/Trainout.xlsx')
X_test = pd.read_excel('C:/Users/sinf5/Desktop/Sampreeth/NewIdea-Attempt1/ML_DATA/Test-Input/TestInput.xlsx')
Y_test = pd.read_excel('C:/Users/sinf5/Desktop/Sampreeth/NewIdea-Attempt1/ML_DATA/Test-Output/Testout.xlsx')

Y_test = Y_test.T
Y_train = Y_train.T

Testsize = 100



def ErrorFun(TS_temp):
    if TS_temp!=0:
        return mean_squared_error((Y_test.iloc[TS_temp-1:TS_temp,:]),(KNR.predict(X_test.iloc[TS_temp-1:TS_temp,:])))+ErrorFun(TS_temp-1)
    else:
        return 0


kNeighbors = []
Trainingsize = []
errror = []
# tunning for 'k' and training data size 't'

for k in range(1,X_train.shape[0]+1):
    print(k)
    
    for t in range(k,349):
        KNR = KNeighborsRegressor(k)
        KNR.fit(X_train.iloc[0:t+1,:],Y_train.iloc[0:t+1,:])
        
        error = ErrorFun(Testsize)
        kNeighbors.append(k)
        Trainingsize.append(t)
        errror.append(error)
    
AnalysisData = pd.DataFrame()
AnalysisData.insert(loc=0, column='kNeighbors' , value = kNeighbors)
AnalysisData.insert(loc=1, column='TrainingData size' , value = Trainingsize)
AnalysisData.insert(loc=2, column='Error' , value = errror)