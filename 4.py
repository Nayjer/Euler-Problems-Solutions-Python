#!/usr/bin/python

"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

possible_numbers = []
possible_products = []

for i in range(1,10):
	for k in range(1,10):
		for z in range(1,10):
			possible_numbers.append(int(str(i)+str(k)+str(z))) #generates all 3-digit numbers

for i in possible_numbers:
	for k in possible_numbers:
		possible_products.append(i*k) #generates all products between these numbers

unique_possible_products = list(set(possible_products)) #erases duplicates
unique_possible_products.sort() #orders by size
unique_possible_products.reverse() #reverse it because the biggest palindrone is probably big (just a feeling)

def is_palindrone(number):
	s = str(number)
	count = 0
	for i in range(0, 3): #probably the palindrone is a 6 digit number
		if not s[i] == s[-(i+1)]:
			count += 1
	if count != 0:
		return False
	else:
		return True
	

for i in unique_possible_products: #looks if its a palindrone and how we can notice: it begins at the largest number
	if is_palindrone(i):
		print(i)
		exit()
