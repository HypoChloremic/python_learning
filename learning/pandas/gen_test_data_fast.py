'''Ali Rassolie 2020
Creating test-datasets fast'''

import pandas as pd
import numpy as np

# One way using numpy
def gen_prob_dis(row, col):
	'''Note that np.random.randn is a method that 
	returns a numpy array. The shape of the array is defined by
	the first two parameters. 
	>>> np.random.randn(10,2)
	array([[ 1.21217886,  0.07947556],
	[ 1.12544439,  0.47671354],
	[-2.08624046, -1.00259477],
	[-0.47912411,  2.03311841],
	[ 1.93553099, -0.37742648],
	[-0.18338724, -1.32413324],
	[ 0.00618181, -1.06724402],
	[-1.73775804, -0.56723248],
	[ 0.0453128 , -1.69658481],
	[ 1.0764628 ,  0.40077494]])
	or 
	>>> np.random.randn(1, 10)
	array([[-0.9121891 ,  0.19937912, -0.19446749, -1.16859599,  0.21974883,
	 0.9859165 ,  0.91796506,  0.58438234, -0.05775883, -1.14443478]])
	Hence when combined with pd.DataFrame, it will accordingly return a with 
	the given amount of rows and columns. '''
	return pd.DataFrame(np.random.randn(row, col))


if __name__ == '__main__':
	a = gen_prob_dis(10,2)
	a.columns = ['0', '1']
	print(getattr(a, '0'))

