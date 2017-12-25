#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 19:17:29 2017

@author: xuyizhou
"""

filePath='/Users/xuyizhou/Desktop/after.txt'
fileRead = []
with open(filePath) as fileRaw:
    for line in fileRaw:
        fileRead.append(line)
data=[]
for i in range(len(fileRead)):
  
    data.append(float(fileRead[i]))

sumPlus=0   
for j in range(len(fileRead)-1):
   print("每门课增加")
   print(data[j+1]-data[0])
   sumPlus=data[j+1]-data[0]+ sumPlus
print("刷分后")
#print(sumPlus)
print(sumPlus+data[0])