import os
import numpy as np
from snownlp import SnowNLP
import matplotlib.pyplot as plt



comment_list=[]
new_comment = []
f = open('e:/new_comment2.txt','r')
comment_list = f. readlines()
f.close()

sentiments_list = []
# i =0
for comment in new_comment:
	s = SnowNLP(comment)
	# if(s.sentiments>0.35 and s.sentiments<0.65 ):
	# 	print(comment)
	# 	print(s.sentiments)
	sentiments_list.append(s.sentiments)
	# i = i+1
plt.hist(sentiments_list, bins=np.arange(0,1,0.02))
plt.show()
