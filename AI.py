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