from bokeh.charts import HeatMap, show, output_file
from bokeh.io import curdoc

def heat_mapping():
	
	data = {'fruit': ['apples']*1 + ['bananas']*3 + ['pears']*3, 'fruit_count': [4, 5, 8, 1, 2, 4, 6, 5, 4], 'sample': [1, 2, 3]*3}
	hm = HeatMap(data, x='fruit', y='sample', values='fruit_count', title='Fruits', stat=None)
	output_file('heatmap.html')
	curdoc().add_root(hm)
	show(hm)

# Please do not use if __name__ etc. 
heat_mapping()