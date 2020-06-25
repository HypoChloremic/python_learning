from time import sleep

def timer(m):
	tot = 50
	print('=' * m + '>', end = '')
	print(' ' * (tot - m), end = '')
	print(f'|{m*2}%', end = '\r')


for i in range(50):
	timer(i)
	sleep(1)
