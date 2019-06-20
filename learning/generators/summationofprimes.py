# This problem revolves around finding the sum of all primes
# below 2 million, without wasting memory!!

import math


# def is_prime(num):
# 	if num == 1 or num == 2:
# 		return True
# 	for up_to_number in range(3,int(math.sqrt(num))+1, 2):
# 		if num % up_to_number == 0:
# 			return False
# 	return Exception("We gots a problem")

# def get_prime():
# 	num = 0
# 	while True:
# 		if is_prime(num):
# 			yield num
# 		num += 1

# def summer(length=2000000):
# 	su = 0
# 	for x in range(0,length):
# 		su += next(get_prime())
# 	print(su)


def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0: 
                return False
        return True
    return False


def get_primes(number):
    while True:
        if is_prime(number):
            yield number
        number += 1

def solve_number_10():
    # She *is* working on Project Euler #10, I knew it!
    total = 2
    pos = 0
    for next_prime in get_primes(3):
        
        if next_prime < 2000000:
            total += next_prime
        else:
            print(total)
            return
        pos += 1
if __name__ == '__main__':
	solve_number_10()
