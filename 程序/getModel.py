
import re
import time
import requests


header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'}

color_size = []

for i in range(0,100):
	try:	
		color_list = []
		size_list  = []
		response = requests.get('https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv13060&productId=5089273&score=0&sortType=5&page='+str(i)+'&pageSize=10&isShadowSku=0&rid=0&fold=1',headers =header)
		text = response.text
		pat_color = r'"productColor":"(.*?)",'
		pat_size  = r'"productSize":"(.*?)",'
		color_list = re.findall(pat_color, text)
		size_list  = re.findall(pat_size, text)

		for x in range(0,10):
			color_size.append([color_list[x], size_list[x]])
		
		print("爬取第"+str(i)+"成功")
		time.sleep(1)
		
	except:
		print("爬取第"+str(i)+"出现问题")
		continue

f = open('e:/iphone_model.txt','a')
for iphone in color_size:
	f.write(str(iphone[0])+'\t'+str(iphone[1]))
	f.write('\n')
f.close()



