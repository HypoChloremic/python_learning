from PIL import Image
from pylab import *

im = array(Image.open("002.jpg").convert("L"))
imshow(im)
x = ginput(3)
print(x)
show()
