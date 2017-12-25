#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 00:07:18 2017

@author: xuyizhou
"""
import jieba
clothfilePath='/Users/xuyizhou/Desktop/clothing.txt'
fileDonePath ='/Users/xuyizhou/Desktop/corpus.txt'
clothfileTrainRead = []
#fileTestRead = []
with open(clothfilePath) as clothfileTrainRaw:
    for line in clothfileTrainRaw:
        clothfileTrainRead.append(line)
        
        
fruitfilePath='/Users/xuyizhou/Desktop/fruit.txt'

fruitfileTrainRead = []
#fileTestRead = []
with open(fruitfilePath) as fruitfileTrainRaw:
    for line in fruitfileTrainRaw:
        fruitfileTrainRead.append(line)

fileTrainRead=[]
for i in range(2500):
    fileTrainRead.append(clothfileTrainRead[i])
    fileTrainRead.append(fruitfileTrainRead[i])
   
for i in range(2500):
    fileTrainRead.append(clothfileTrainRead[5000+i])
    fileTrainRead.append(fruitfileTrainRead[5000+i])
with open(fileDonePath,'w') as fW:
    for i in range(len(fileTrainRead)):
        fW.write(str(fileTrainRead[i]))