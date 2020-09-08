import pytesseract as pt
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# 
def return_text(img: 'PIL.Image.open obj') -> str:
	img.show()
	return str(pt.image_to_string(i))


def change_col(
		img: 'PIL.PngImagePlugin.PngImageFile',
		show:bool = True):
	'''
	Accepts a img by using PIL.Image.open method
	When converting to np array from the PIL RGVA 
		-> height x width x 4
	
	By transposing: height x width x 4 -> 4 x height x width
	'''
	im = img.convert('RGBA')
	d = np.array(im) # read the data
	r,g,b,a = d.T # can be used due to transposition.
	
	# Identify the green areas
	green_areas = (r < 255) & (b < 125) & (g > 124)
	
	# TODO: find out what the dot dot dot does in python slices
	# we retranspose the matrix, such that the indices will correspond
	d[...,:-1][green_areas.T] = (255,255,255)
	new_im = Image.fromarray(d)

	if show: new_im.show()
	return new_im

if __name__ == '__main__':
	USER = 'random'
	CMD_PATH = f'C:\\Users\\{USER}\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'
	p = 'imgs\\r1.PNG'

	pt.pytesseract.tesseract_cmd = CMD_PATH
	i = Image.open(p)
	i2 = change_col(i, show=False)
	print(return_text(i2))
