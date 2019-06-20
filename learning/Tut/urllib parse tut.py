import urllib.request

# urllib.parse is used to parse values into the url
import urllib.parse

'''
Worth noting:
url = "http://blabla.com"
urllib.parse.urlencode does the following:
Create a dictionary: a = {"Hello":"There", "What":"Is"}
x = urllib.parse.urlencode(a)
Thus x = 'Hello=There&What=Is'
x = x.encode("utf-8") implies that the data will be encoded in bytes
req = urllib.request.Request(url, x) This will combine the url and x into a request
resp = urllib.request.urlopen(req)This will open the req url
'''





url = "http://pythonprogramming.net"
values = {"s":"basic", "submit":"search"}


