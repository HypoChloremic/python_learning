import urllib.request
import urllib.parse
import re

url = "http://texttv.nu/104"
a = urllib.request.urlopen(url)
x = str(a.read())
paragraphs = re.findall(r'<span class="W">(.*?)</span>', str(x))

file = open('x.txt', 'w')
file.write(x)
file.close()

for eachP in paragraphs:
    print(eachP)

