# historgram

def histogram(s):
	d = dict()
	for c in s:
		a = d.get(c, 0) 
		d[c] = 1+a
	return sorted(d)
h = histogram("brantosaurus")
print(h)