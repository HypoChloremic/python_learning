# Text Analysis
# (c) 2017 Ali Rassolie

import os, collections, re, argparse, sys, codecs
import pyautogui as pg
import PyPDF2 as p


class Tan:
	def __init__(self, basepath="C:\\dfm2_tentor", total=16):
	# Encoding 

		self.basepath = basepath
		self.total_count = collections.Counter()
		self.data_handling()

	def data_handling(self):
		alt_names = ["REST", "ORD"]
		# Very ugly indeed
		base_name   = [["VT1{}".format(x), "HT1{}".format(x)] for x in range(3,7)]
		name = [[base_name[x][x%2]+" ORD", base_name[x][x%2]+" REST", base_name[x][(x+1)%2]+" ORD", base_name[x][(x+1)%2]+" REST"] for x in range(len(base_name)) ]

		for pos in name:
			for x in range(4):
				filename = pos[x]+".pdf"
				self.full_path ="{}\\{}".format(self.basepath, filename)
				new_counter = next(self.data_generator())
				self.total_count = self.total_count + new_counter
				print(self.total_count)

		with open("dfm2tentoran.txt", "wb") as file:
			output_text = str()
			for each in iter(self.total_count):
				output_text += "\n {}: {} \n".format(each, self.total_count[each])
			output_text = output_text.replace("å","a").replace("ä","a").replace("ö","o")	
			
			print(output_text)
			file.write(output_text.encode())

	def data_generator(self):
	# A generator which yields a counter,
	# the counter is then merged with the total_counter, which is then 
	# printed to a txt file for analysis
		text = str()
		while True:
			path = self.full_path
			with open(path, "rb") as file:
				data = file
				print(data)
				decoded_pdf_data = p.PdfFileReader(data)
				for page_pos in range(decoded_pdf_data.numPages):
					obj = decoded_pdf_data.getPage(page_pos)
					text += obj.extractText()

				words = re.findall(r'\w+', text.lower().replace("\n"," ").replace("å","a").replace("ä","a").replace("ö","o"))
				counted_words = collections.Counter(words)
				print(counted_words.most_common(5))
				yield counted_words

	def datagrabber(self):


if __name__ == '__main__':

	run_instance = Tan()