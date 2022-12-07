# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 11:33:41 2022

@author: sinf5
"""
import pandas as pd
df_data = pd.DataFrame()

df_data = pd.read_excel('C:/Users/sinf5/Desktop/Sampreeth/NewIdea-Attempt1/ML_DATA/kNN_Analysis.xlsx')
loc = 0
tempmin = 100
for i in range(df_data.shape[0]):
    if df_data.iloc[i,3]<tempmin:
        print(df_data.iloc[i,3])
        tempmin = df_data.iloc[i,3]
        loc = i