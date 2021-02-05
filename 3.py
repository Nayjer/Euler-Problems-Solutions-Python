#!/usr/bin/python

"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

def is_prime(number):
	count = 0	
	for i in range(3, int(number**0.5//1), 2): #checks if number is divisible by an uneven number under the square root of the number, if yes its not a prime
		if number % i == 0:
			return False
	if count == 0:
		return True

maximum = int(600851475143**0.5//1) #max possible prime is a number under the square root of the number
print(maximum)

for i in range(maximum,0, -1): #begins from the max possible divisor, checks if its a prime and if yes, checks if its divisble
	if is_prime(i):
		if 600851475143 % i == 0:
			print(i)
			exit()
