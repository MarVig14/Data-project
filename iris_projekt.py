# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import pandas as pd
print(os.getcwd())

path = 'C:\\Users\\Marián\\OneDrive\\Dokumenty\\Programming\\Machine Learning'
os.chdir(path)
print('Actual wd is:'+os.getcwd())

iris = pd.read_csv('IRIS.csv')
iris.tail(3)
iris.info()

from sklearn import preprocessing
label_encoder=preprocessing.LabelEncoder()
iris['species_encoded']=label_encoder.fit_transform(iris['species'])

