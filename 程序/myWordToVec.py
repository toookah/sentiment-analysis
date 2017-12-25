# 转换成词向量
import word2vec
word2vec.word2vec('/Users/xuyizhou/Desktop/corpusSegDone.txt', '/Users/xuyizhou/Desktop/corpusWord2Vec.bin', size=300,verbose=True)
model = word2vec.load('/Users/xuyizhou/Desktop/corpusWord2Vec.bin')
print (model.vectors)

#9000条评论 每条140个词 每个词一个索引 一个索引对应一行矩阵

import tensorflow as tf
import numpy as np
m=len(fileTrainSeg)
n=60
firstSen=np.zeros((m,n),dtype='int32')
#for j in range(len(fileTrainSeg)):
for j in range(m):
    print(j)
    #如果某评论词数小于60
    if len(fileTrainSeg[j][0].split())<=60:
        for i in range(len(fileTrainSeg[j][0].split())):
            index=np.where(model.vocab==fileTrainSeg[j][0].split()[i])[0]

            
            if index>=0:
                if index<=2545:
                    firstSen[j][i]=int(index)
            else:
                firstSen[j][i]=0
            
    else:
    #如果某评论词数大于60
        for i in range(60):
            index=np.where(model.vocab==fileTrainSeg[j][0].split()[i])[0]

            
            if index>=0:
                if index<=2545:
                    firstSen[j][i]=int(index)
            else:
                firstSen[j][i]=0
            
print("索引矩阵：")
print(firstSen)
#得到每一行的词语数量
numWords=[]
for i in range(len(fileTrainSeg)):
    counter = len(fileTrainSeg[i][0].split())
    numWords.append(counter)   
    
print('The total number of words in the files is', sum(numWords))
#
import matplotlib.pyplot as plt
#matplotlib inline
plt.hist(numWords, 50)
plt.xlabel('Sequence Length')
plt.ylabel('Frequency')
plt.axis([0, 150, 0, 4000])
plt.show()
