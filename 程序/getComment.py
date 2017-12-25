import os
import re
import time
import requests
import pandas as pd 

header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'}

comment= []
iphone = []
model=[]
f = open('e:/comment_iphone8plus.txt','a')
for i in range(0,500):
	try:
		
		response = requests.get('https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv13060&productId=5089273&score=0&sortType=5&page='+str(i)+'&pageSize=10&isShadowSku=0&rid=0&fold=1')
		text = response.text
		pat1 = '"content":"(.*?)","'
		

		res_comment = re.findall(pat1, text)
		for com in res_comment:
			com = com.replace('\\n','')
			if com not in comment:
				comment.append(com)
				f.write(com)
				f.write('\n')
		
		print("爬取第"+str(i)+"成功")
		time.sleep(3)
	except:
		print("爬取第"+str(i)+"出现问题")
		continue
f.close()
#gold = 0
#sliver = 0
#f = open('e:/model_iphone.txt','a')
#for ip in model:
#	f.writeline(ip)
#	if(ip[0] == '金色'):
#		gold += 1
#	if (ip[0] == '银色'):
#		sliver += 1
#	if (ip[0] == '深空灰色'):
#		gray += 1
# f.close()
# print("gray = ", gray)
# print("gold = ", gold)
# print("sliver = ", sliver)