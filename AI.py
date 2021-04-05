# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 14:34:26 2021

@author: PC
"""

# AI/WeatherAUS.py
# for linear algebra (library of linear algebra)
import numpy as np

# for data processing (library of data processing)
import pandas as pd

# load the data set (import data)
df = pd.read_csv('./weatherAUS.csv')

# display the shape of the data set
print('độ lớn của bảng [frame] dữ liệu thời tiết:',df.shape)

#display data (hiển thị dữ liệu mảng 5 dòng đầu)
print(df[0:5])

# exercise with data
# checking for null value ,if null count lines of property of that
print(df.count().sort_values())

df =df.drop(columns =['Sunshine','Evaporation','Cloud3pm','Cloud9am','Location','Date','RISK_MM'],axis=1)
print(df.shape)

# drop the collum of null value
df =df.dropna(how='any')
print(df.shape)

print('------------------xử lý ngoại lệ----------------')
# Thư viện xử lý DL ngoại lệ
from scipy import stats
import scipy.stats as stats

#kiểm tra tập dữ liệu có bất kỳ ngoại lệ nào không
print('------kiểm tra ngoại lệ ------------')
z = np.abs(stats.zscore(df._get_numeric_data()))
print(z)
df= df[(z < 3).all(axis=1)] 
print(df.shape)
# from stats import zscore

print("-----------zscore----------")
a =stats.zscore(z)
print(a)

#Thay thế yes and no vào vị trí giá trị 1 và 0 tương ứng cột|biến RainToday và RainTomorrow
df['RainToday'].replace({'No': 0, 'Yes': 1},inplace = True)
df['RainTomorrow'].replace({'No': 0, 'Yes': 1},inplace = True)

# Thư viện chuẩn hóa DL
from sklearn import preprocessing
# CHUẨN HÓA DL
scaler = preprocessing.MinMaxScaler()
scaler.fit(df)
df = pd.DataFrame(scaler.transform(df), index=df.index, columns=df.columns)
df.iloc[4:10]
print(df)



