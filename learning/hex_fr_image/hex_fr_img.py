from pylab import *

cmap = cm.get_cmap('tab20')

for i in range(cmap.N):
	rgb = cmap(i)[:3]
	print(matplotlib.colors.rgb2hex(rgb))