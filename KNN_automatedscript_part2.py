# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 09:17:20 2022

@author: sinf5
"""

from keras.models import Sequential
from keras.layers import Dense
from sklearn.neighbors import KNeighborsRegressor 
from sklearn.linear_model import LinearRegression 
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
import random

from shapely.geometry import Polygon
import matplotlib.pyplot as plt


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


KNR = KNeighborsRegressor(15)
KNR.fit(X_train.iloc[0:344,:],Y_train.iloc[0:344,:])






i=0
status = True
df_input = pd.DataFrame(columns=['x1','x2','x3','x4','y1','y2','y3','y4'])
df_predoutput = pd.DataFrame() 
while status == True:
    # print(i)
    x1 = []
    x2 = []
    x3 = []
    y1 = []
    y2 = []
    y3 = []
    x4=[]
    y4=[]
    pred= []
    
    y1.append(round(random.uniform(-27.5, 17.5),1))
    if y1[0]>-18.5:
        x1.append(round(random.uniform(-62.5,0),1))
    else:
        x1.append(round(random.uniform(-62.5,-6),1))
        
    x2.append(round(random.uniform(-62.5, 0),1))
    y2.append(round(random.uniform(17.5, 62.5),1))
    
    x3.append(round(random.uniform(0, 62.5),1))
    y3.append(round(random.uniform(17.5,62.5),1))
    
    y4.append(round(random.uniform(-27.5, 17.5),1))
    if y4[0]>18.5:    
        x4.append(round(random.uniform(0, 62.5),1))
    else:
        x4.append(round(random.uniform(6, 62.5),1))

    
    
    df_input.loc[i,'x1'] = x1[0]
    df_input.loc[i,'x2'] = x2[0]
    df_input.loc[i,'x3'] = x3[0]
    df_input.loc[i,'x4'] = x4[0]
    df_input.loc[i,'y1'] = y1[0]
    df_input.loc[i,'y2'] = y2[0]
    df_input.loc[i,'y3'] = y3[0]
    df_input.loc[i,'y4'] = y4[0]
    
    

    
    pred = KNR.predict(df_input.iloc[i:i+1,:])
    
    for j in range(pred.shape[1]):
        if pred[0][j]>0.5:
            pred[0][j]=1
        else:
            pred[0][j]= 0
    df_temp =   pd.DataFrame(pred)
    df_predoutput= pd.concat([df_predoutput,df_temp])
    
    #condition-1
    # if df_predoutput.iloc[i,:].sum(axis=0) > 7:
    #     print("Bingo", df_input.iloc[i,:].T)
    #     status=False
        
    #condition-2
    BW=7
    a=0
    while a< (df_predoutput.shape[1]):
        check_BW=0
        if df_predoutput.iloc[i,a] == 1:
            b=a
            while b<df_predoutput.shape[1] and df_predoutput.iloc[i,b]==1:
                check_BW+=1
                b+=1
                a=b
        # 
        if check_BW==BW:
            status=False
            print('\nindex: ',i,'\n\nSuitable points: ',df_input.iloc[i,:],'\n\nBW: ',check_BW)
            
            #Drawing the design
            plt.rcParams["figure.figsize"] = [7, 5]
            plt.rcParams["figure.autolayout"] = True
            polygon1 = Polygon([(0, 0),(55.90, 0),(55.90,35),(0,35)])
            polygon2 = Polygon([(69.1, 0),(125, 0),(125,35),(69.1,35)])
            polygon3 = Polygon([(56.5, 0),(68.5, 0),(68.5,44.25),(56.5,44.25)])
            X1,X2,X3,X4,Y1,Y2,Y3,Y4 = (df_input.iloc[i,:].to_string(index=False)).split('\n')
            polygon4 = Polygon([(sum(x1)+62.5,sum(y1)+62.5),(sum(x2)+62.5,sum(y2)+62.5),(sum(x3)+62.5,sum(y3)+62.5),(sum(x4)+62.5,sum(y4)+62.5),(68.5,44.25),(56.5,44.25)])
            plt_x, plt_y = polygon1.exterior.xy
            plt_x2, plt_y2 = polygon2.exterior.xy
            plt_x3, plt_y3 = polygon3.exterior.xy
            plt_x4, plt_y4 = polygon4.exterior.xy
            plt.plot(plt_x, plt_y, c="red")
            plt.plot(plt_x2, plt_y2, c="red")
            plt.plot(plt_x3, plt_y3, c="red")
            plt.plot(plt_x4, plt_y4, c="red")
            plt.show()
        else:
            print('\nindex: ',i)
            
        a+=1
        
    i=i+1
