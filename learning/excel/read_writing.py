import panda as pd
import numpy as np



if __name__ == '__main__':
	d = pd.ExcelFile('filename.xlsx')
	print(d.sheet_names)
	d1 = d.parse('sheetname of intererst')