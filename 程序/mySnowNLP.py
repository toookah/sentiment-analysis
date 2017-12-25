#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 21:34:10 2017

@author: xuyizhou
"""
#导入SnowNLP包
from snownlp import SnowNLP
import pandas as pd
#读入数据集
df=pd.read_excel('trainData.xlsx')
count = 0
#对读入数据进行基本操作
df.head()
df.head(1)
df.dtypes
df.index
df.describe
df.iloc[3:5,1:4]
#利用SnowNLP处理数据
while (count < 3):
   print ("The count is:", str(df.iloc[count,1]))
   strdata=str(df.iloc[count,1])

   s = SnowNLP(strdata)
   print("---------------")
   print(s.words)
   print("---------------")
   count = count + 1
print ("Good bye!")
#对得到的s进行操作
s.words

#
#print(arr[0])
#['质量好', '做工也不错', '尺码标准', '']
#
#print(arr[0][1])
#做工也不错
#
    
"""
df=pd.read_excel('trainData.xlsx')
count = 0
while (count < 3):
   print ("The count is:", str(df.iloc[count,1]))
   strdata=str(df.iloc[count,1])
   s = SnowNLP(strdata)
   print("---------------")
   print(s.words)
   print("---------------")
   count = count + 1

print ("Good bye!")
"""