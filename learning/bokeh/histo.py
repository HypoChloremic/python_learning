# Running annuc
# (c) 2017 Ali Rassolie
# Important to note that this has to be run in the command line environment
# bokeh serve --show first_plot.py


from collections import OrderedDict
from bokeh.charts import Bar, output_file, show
from bokeh.io import curdoc

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 
import annuc

def histo_bokeh(infile=None):
	with open(infile, "r") as file:
		info  = [ line.replace("\n", "") for line in file ]
	
	combo = [ combo.split("\t")[0] for combo in info  ]
	amount = [ int(appearances.split("\t")[1]) for appearances in info  ]

	data_as_dict = { combo[pos]: amount[pos] for pos in range(len(combo)) }
	

	ordered_data_as_dict = OrderedDict(data_as_dict)
	ordered_data_as_dict = pd.Series(ordered_data_as_dict, index=ordered_data_as_dict.keys())
	bar = Bar(ordered_data_as_dict, title="Stacked bars")
	output_file("stacked_bar.html")
	curdoc().add_root(bar)
	show(bar)

histo_bokeh(infile="malbac_0_counter.vcf")

