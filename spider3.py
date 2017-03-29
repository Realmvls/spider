# -*- coding : UTF-8 -*-
import re
import requests

url = "http://www.vhiphop.com/"
html = requests.get(url).text
names = re.findall(r'<li><a href="(.*?)</a></li>',html,re.S)
for name in names:
    print name