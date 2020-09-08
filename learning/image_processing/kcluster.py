import numpy as np
from scipy.cluster.vq import * 

class1 = 1.5*np.random.randn(100,2)
class2 = np.random.randn(100,2) + np.array([5,5])
features = np.vstack((class1,class2)) # vstack stacks the arrays
                                      # In essence, the function will take the
                                      # two arrays will be stacked one after the other
                                      # if one is 5 columns, the second is 2 columns
                                      # after vstack, the new array will be 7 columns,
                                      # one after the other. 

centroids, variance = kmeans(features,2) # centroids is an array of values, whereas the variance is solely one value
print (variance)
