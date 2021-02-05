#!/usr/bin/python

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

i = 2520 #we can begin here, because of course the number that is divisble from 1 to 20 is bigger

while True:
	print(i)
	count = 0
	for k in range(1,21):
		if i % k == 0:
			count += 1
	if count == 20:
		print(i)
		exit()
	else: #we can make 20s step because the number needs to be divisble by 20, if we want more efficience we could influence some more divisibility rules 
		i += 20	
