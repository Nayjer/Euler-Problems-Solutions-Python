#!/usr/bin/python

#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.


max_number = 1000
multiple1 = 3
multiple2 = 5

sum_of_multiples = 0

for i in range (1, max_number):
	if i % multiple1 == 0:
		sum_of_multiples += i
	elif i % multiple2 == 0:
		sum_of_multiples += i
	
print(sum_of_multiples)
