#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 12:08:44 2017

@author: xuyizhou
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA
import word2vec
# load the word2vec model
model = word2vec.load('/Users/xuyizhou/Desktop/corpusWord2Vec.bin')
rawWordVec=model.vectors

# reduce the dimension of word vector
X_reduced = PCA(n_components=2).fit_transform(rawWordVec)
 
# show some word(center word) and it's similar words
index1,metrics1 = model.cosine(u'好')
index2,metrics2 = model.cosine(u'差')
index3,metrics3 = model.cosine(u'快递')
index4,metrics4 = model.cosine(u'苹果')
index5,metrics5 = model.cosine(u'衣')
index6,metrics6 = model.cosine(u'京东')

 # add the index of center word 
index01=np.where(model.vocab==u'好')
index02=np.where(model.vocab==u'差')
index03=np.where(model.vocab==u'快递')
index04=np.where(model.vocab==u'苹果')
index05=np.where(model.vocab==u'衣')
index06=np.where(model.vocab==u'京东')

index1=np.append(index1,index01)
index2=np.append(index2,index03)
index3=np.append(index3,index03)
index4=np.append(index4,index04)
index5=np.append(index5,index05)
index6=np.append(index6,index06)

 # plot the result
zhfont = matplotlib.font_manager.FontProperties(fname='/System/Library/Fonts/PingFang.ttc')
fig = plt.figure()
ax = fig.add_subplot(111)

for i in index1:     
    ax.text(X_reduced[i][0],X_reduced[i][1], model.vocab[i], fontproperties=zhfont,color='r')  
for i in index2:     
    ax.text(X_reduced[i][0],X_reduced[i][1], model.vocab[i], fontproperties=zhfont,color='b')    
for i in index3:     
    ax.text(X_reduced[i][0],X_reduced[i][1], model.vocab[i], fontproperties=zhfont,color='g')
for i in index4:     
    ax.text(X_reduced[i][0],X_reduced[i][1], model.vocab[i], fontproperties=zhfont,color='k')
for i in index5:     
    ax.text(X_reduced[i][0],X_reduced[i][1], model.vocab[i], fontproperties=zhfont,color='c')
for i in index6:     
    ax.text(X_reduced[i][0],X_reduced[i][1], model.vocab[i], fontproperties=zhfont,color='y')
ax.axis([-0.4,1,-1,1])
plt.show()