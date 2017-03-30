# -*- coding : UTF-8 -*-
import re
import requests

url = "http://www.vhiphop.com/"
html = requests.get(url).text
names = re.findall(r'<a.*?href=.*?</a>', html, re.I|re.S|re.M)
for name in names:
    print name