# Automating downloads from website;
# this is the result after realizing
# that the css-selectors for the site 
# were highly inadequate for bs4.
# (c) 2017 Ali Rassolie

import pyautogui as pg
import time

class Auto:
	def __init__(self):
		pg.moveTo(530, 115)
		pg.click()
		self.gen = self.main_page()
		self.download()

	def download(self):
		# Moving the mouse to the center
		x = 65
		for pos in range(20):
			time.sleep(5)
			# Download
			pg.moveTo(1823,117)
			pg.click()
			time.sleep(2)
			# Save
			pg.moveTo(1310,667)
			time.sleep(2)
			pg.click()
			# back
			pg.moveTo(17,51)
			pg.click()
			time.sleep(4)
			# new document
			pg.moveTo(530, 115+x)
			pg.click()
			x += 75

	def main_page(self):
		pos = 0
		print("wu")
		while True:
			print("wu")
			yield pg.moveTo(530, 265+pos)
			pos += 30

if __name__ == '__main__':
	a  = Auto()