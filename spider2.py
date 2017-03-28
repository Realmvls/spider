#-* - coding: UTF-8 -* -
import re
import requests
#读取源代码文件
f = open('1.html','r')
html = f.read()
f.close()
#进行正则匹配
pic_url = re.findall('src="(.*?)" alt',html,re.S)
i = 0
#保存本地
for each in pic_url:
    print 'now downloading:'+ each
    pic = requests.get(each)
    fb = open('pic\\'+str(i )+'.jpg','wb')
    fb.write(pic.content)
    fb.close()
    i += 1
