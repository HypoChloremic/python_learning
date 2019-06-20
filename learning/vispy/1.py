from vispy.plot import Fig
import numpy as np

fig = Fig(bgcolor='p', size=(800, 600), show=True)
left = fig[0,0]
right = fig[0,1]
data = np.random.randn(2,2)

left.plot(data)
right.histogram(data[1])
