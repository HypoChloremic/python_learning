from collections import OrderedDict
from bokeh.charts import Bar, output_file, show
from bokeh.io import curdoc
import pandas as pd

# (dict, OrderedDict, lists, arrays and DataFrames are valid inputs)
xyvalues = OrderedDict([('G>T', 34311), ('A>G', 78828), ('C>T', 48809), ('T>A', 45507), ('G>A', 48207), ('C>A', 34614), ('T>G', 15244), ('A>C', 14984), ('C>G', 13716), ('G>C', 13367), ('A>T', 44795), ('T>C', 78768)])
xyvalues = pd.Series(xyvalues, index=xyvalues.keys())
bar = Bar(xyvalues, title="Stacked bars")
output_file("stacked_bar.html")
curdoc().add_root(bar)
show(bar)