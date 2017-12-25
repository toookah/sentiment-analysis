# -*- coding: utf-8 -*-  
import os
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

f = open("e:/iphone_model.txt",'r')
color_size = []
for line in f.readlines():
	line = line.split('\t')
	color_size.append([line[0], line[1].replace('\n','')])


gray  = 0
gold  = 0	
slive = 0
gr_64 = 0
gr_256 = 0
go_64 = 0
go_256 =0
s_64 = 0
s_256 = 0

gb64 = 0
gb256 =0

for iphone in color_size:
	if(iphone[0] == '银色'):
		if(iphone[1] == '64GB'):
			s_64+=1
		else:
			s_256+=1
		slive+=1 
	elif(iphone[0] == '深空灰色'):
		if(iphone[1] == '64GB'):
			gr_64+=1
		else:
			gr_256+=1
		gray+=1
	elif(iphone[0] == '金色'):
		if(iphone[1] == '64GB'):
			go_64+=1
		else:
			go_256+=1
		gold+=1
	else:
		pass
gb64 = gr_64 + go_64 +s_64
gb256 = gr_256 + go_256 +s_256


labels=['64GB', '256GB']

X=[gb64, gb256]    
  
fig = plt.figure()  
plt.pie(X,labels=labels,autopct='%1.2f%%') #画饼图（数据，数据对应的标签，百分数保留两位小数点）  
plt.title("size of iphone8 plus Pie chart")  
    
  
plt.show()   
