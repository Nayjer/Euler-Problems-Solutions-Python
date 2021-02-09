#!/usr/bin/python3

import math

i = 1 

while True:
	divisors = 0
	triangle_number = int(i*(i+1)*0.5)
	for k in range(1, int(math.sqrt(triangle_number)//1)):
		if triangle_number % k == 0:
			divisors += 2
	if divisors > 500:
		print(triangle_number)
		exit()
	else:
		i += 1
