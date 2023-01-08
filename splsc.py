#importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
#first we will set our x as independent variable and y as target variable
y=data.iloc[:,0]
x=data.iloc[:,1:23]
#now we will give 70 percent data for training and 30 percent for test
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
x_train.shape
x_test.shape
#now we will use some technique of feature scalling
scale=preprocessing.StandardScaler()
x_train=scale.fit_transform(x_train)
x_train
y_train=scale.fit_transform(y_train)
y_train
x_test=scale.fit_transform(x_test)
x_test
y_test=scale.fit_transform(y_test)
y_test
#Now are data is processed and ready to be modelled
