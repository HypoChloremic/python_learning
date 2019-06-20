# Stacked bars
# (c) Ali Rassolie

from collections import OrderedDict
from bokeh.charts import Bar, output_file, show
from bokeh.charts.operations import blend
from bokeh.charts.attributes import cat, color
from bokeh.io import curdoc

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 

def stack_bokeh(infile):
	with open(infile, "r") as file:
		data = pd.read_csv(file)
	print(data)
	
	p = Bar(data,
	          values=blend('locus dropout', 'allelic dropout', 'biallelic coverage', name='samp', labels_name="samps"),
	          label=cat(columns='Sample', sort=False),
	          stack=cat(columns='samps', sort=False),
	          color=color(columns="samps", palette=["green", "red", "black"], sort=False),
	          legend='top_right',
	          title="sam")




	output_file("stacked_bar.html")
	curdoc().add_root(p)
	show(p)


stack_bokeh("test_data.csv")
