#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 23:34:04 2017

@author: xuyizhou
"""
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
sess=tf.InteractiveSession()

x=tf.placeholder(tf.float32,[None,784])
W=tf.Variable(tf.zeros([784,10]))
b=tf.Variable(tf.zeros([10]))
y=tf.nn.softmax(tf.matmul(x,W)+b)
y_=tf.placeholder(tf.float32,[None,10])


cross_entropy=tf.reduce_mean(-tf.reduce_sum(y_ *tf.log(y),reduction_indices=[1]))
train_step=tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
tf.global_variables_initializer().run()
for i in range(1000):
    batch_xs,batch_ys=mnist.train.next_batch(100)
    train_step.run({x:batch_xs,y_:batch_ys})
correct_pre=tf.equal(tf.argmax(y,1),tf.argmax(y_,1))
accu=tf.reduce_mean(tf.cast(correct_pre,tf.float32))
print(accu.eval({x:mnist.test.images,y_:mnist.test.labels}))