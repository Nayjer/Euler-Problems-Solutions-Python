#!/usr/bin/python3

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

import sympy

i = 2
sum_of_primes = 0

while i < 2000000:
	if sympy.isprime(i):
		sum_of_primes += i
	i += 1

print(sum_of_primes)
