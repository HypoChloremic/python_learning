
import os, collections, re, argparse, sys, codecs
import PyPDF2 as p



def names():
	alt_names = ["REST", "ORD"]
	# Very ugly indeed
	base_name   = [["VT1{}".format(x), "HT1{}".format(x)] for x in range(3,7)]
	name = [[base_name[x][x%2]+" ORD", base_name[x][x%2]+" REST", base_name[x][(x+1)%2]+" ORD", base_name[x][(x+1)%2]+" REST"] for x in range(len(base_name)) ]

	for pos in name:
		for x in range(4):
			print(pos[x])

def data(filepath=None, basepath="C:\\dfm2_tentor"):
	text = str()
	path = basepath+"\\VT16 REST.pdf"
	
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
		
		with open("data3.txt", "wb") as file2:
			output_text = str()
			for each in iter(counted_words):
				output_text += "\n {}: {} \n".format(each, counted_words[each])

			file2.write(output_text.encode())
		with open("str.txt", "wb") as file3:
			file3.write(text.encode())
if __name__ == '__main__':
	data()