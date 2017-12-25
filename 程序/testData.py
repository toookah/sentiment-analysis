#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 17:11:53 2017

@author: xuyizhou
"""

#优化器
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=prediction, labels=labels))
optimizer = tf.train.AdamOptimizer(learning_rate=0.01).minimize(loss)

#可视化

#训练
tf.summary.scalar('Loss', loss)
tf.summary.scalar('Accuracy', accuracy)
merged = tf.summary.merge_all()

sess = tf.InteractiveSession()
saver = tf.train.Saver()
sess.run(tf.global_variables_initializer())

writer = tf.summary.FileWriter("/tmp/mnist_logs", sess.graph)#logdir


for i in range(1950):#iterations
   #Next Batch of reviews
   nextBatch, nextBatchLabels = getTrainBatch();
   sess.run(optimizer, {input_data: nextBatch, labels: nextBatchLabels})
   """
   xyz
   if (i % 50 == 0):   
       print(sess.run(loss, {input_data: nextBatch, labels: nextBatchLabels}))

   if (i % 100 == 0):  
       print(i, sess.run(weight), sess.run(bias))
   """
   #Write summary to Tensorboard
   if (i % 50 == 0):
       print(i)
       summary = sess.run(merged, {input_data: nextBatch, labels: nextBatchLabels})
       writer.add_summary(summary, i)

   #Save the network every 10,000 training iterations
save_path = saver.save(sess, "models/pretrained_lstm.ckpt", global_step=i)
print("saved to %s" % save_path)
writer.close()

