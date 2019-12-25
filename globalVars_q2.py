# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 01:25:32 2019

@author: Sadman Sakib
"""
import pandas as pd
#Declare all global variables
# loading datasets
dfTrain = pd.read_csv("q2_train.csv")
dfTest = pd.read_csv("q2_test.csv")
valuesFullDS=dict()
X = dfTrain.iloc[:, 0:len(dfTrain.columns)-1] 	  
y = dfTrain['class'] 	  
posterior_P=0
posterior_N=0
individualLikelyhood=0
allColumns=list(X.columns.values)
likelyhood_P=dict()
likelyhood_N=dict()
X_test=dfTest.iloc[:, 0:len(dfTrain.columns)-1] 
Y_test=dfTest['class']	
labels=['POSITIVE','NEGATIVE']
