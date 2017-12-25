#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 00:14:12 2017

@author: xuyizhou
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 21:35:55 2017

@author: xuyizhou

索引矩阵：
[[   8    7  106 ...,    0    0    0]
 [  10    8    3 ...,    0    0    0]
 [  52    3    7 ...,    0    0    0]
 ..., 
 [  30 1720  157 ...,    0    0    0]
 [ 166   68    1 ...,    0    0    0]
 [  92   19   15 ...,    0    0    0]]
"""

#下面你可以找到几个辅助函数，这些函数在稍后训练神经网络的步骤中会使用到。
from random import randint

def getTrainBatch():
    labels = []
    arr = np.zeros([batchSize, maxSeqLength])
    for i in range(batchSize):
        if (i % 2 == 0): 
            num = randint(1,4000)
            labels.append([1,0])
        else:
            num = randint(6001,10000)
            labels.append([0,1])
        ids=firstSen
        arr[i] = firstSen[num-1:num]
    return arr, labels

def getTestBatch():
    labels = []
    arr = np.zeros([batchSize, maxSeqLength])
    for i in range(batchSize):
        num = randint(4001,6000)
        if (num <= 5001):
            labels.append([1,0])
        else:
            labels.append([0,1])
        arr[i] = firstSen[num-1:num]
    return arr, labels
#RNN模型
batchSize = 24
lstmUnits = 64
numClasses = 2
iterations = 100000

#LSTM单元的数量
maxSeqLength=60
#词向量维度
numDimensions=50

import tensorflow as tf
tf.reset_default_graph()

#标签占位符
labels = tf.placeholder(tf.float32, [batchSize, numClasses])
#输入占位符
input_data = tf.placeholder(tf.int32, [batchSize, maxSeqLength])

data = tf.Variable(tf.zeros([batchSize, maxSeqLength, numDimensions]),dtype=tf.float32)
data = tf.nn.embedding_lookup(model.vectors,input_data)

lstmCell = tf.contrib.rnn.BasicLSTMCell(lstmUnits)
lstmCell = tf.contrib.rnn.DropoutWrapper(cell=lstmCell, output_keep_prob=0.75)
value, _ = tf.nn.dynamic_rnn(lstmCell, data, dtype=tf.float64)

"""
dynamic RNN 函数的第一个输出可以被认为是最后的隐藏状态向量。这个向量将被重新确定维度，
然后乘以最后的权重矩阵和一个偏置项来获得最终的输出值。
"""
weight = tf.Variable(tf.truncated_normal([lstmUnits, numClasses]),dtype=tf.float32)
bias = tf.Variable(tf.constant(0.1, shape=[numClasses]))
value = tf.transpose(value, [1, 0, 2])
last = tf.gather(value, int(value.get_shape()[0]) - 1)

last = tf.cast(last, tf.float32)#bug1 thx!

prediction = (tf.matmul(last, weight) + bias)
correctPred = tf.equal(tf.argmax(prediction,1), tf.argmax(labels,1))
accuracy = tf.reduce_mean(tf.cast(correctPred, tf.float32))
