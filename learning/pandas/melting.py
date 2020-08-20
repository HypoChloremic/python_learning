import pandas as pd
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

# fake up some data
spread = np.random.rand(50) * 100
center = np.ones(25) * 50
flier_high = np.random.rand(10) * 100 + 100
flier_low = np.random.rand(10) * -100

data = np.concatenate((spread, center, flier_high, flier_low))
data = pd.DataFrame([data, data]).T

'''
            0          1
0   70.036730  70.036730
1   74.275081  74.275081
2   70.928001  70.928001
3   56.674552  56.674552
4   97.778533  97.778533
..        ...        ...
90 -92.717429 -92.717429
91 -61.465203 -61.465203
92 -60.906377 -60.906377
93 -68.468487 -68.468487
94 -25.101297 -25.101297

[95 rows x 2 columns]
'''

pd.melt(data)

'''
     variable      value
0           0  70.036730
1           0  74.275081
2           0  70.928001
3           0  56.674552
4           0  97.778533
..        ...        ...
185         1 -92.717429
186         1 -61.465203
187         1 -60.906377
188         1 -68.468487
189         1 -25.101297

[190 rows x 2 columns]
'''