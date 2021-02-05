#!/usr/bin/python3

import sympy

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""

count = 1
k = 3

while True:
	print(count)
	if sympy.isprime(k):
		count += 1 #if k is prime we add 1 to count, so if count = 10001 we have our 10001st prime number
	elif count == 10001:
		print(k-2)
		exit()
	k += 2
