"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

def abundant_number(number):
	proper_divisors = []
	for i in range(1, number):
		if number % i == 0:
			proper_divisors.append(i)
	if sum(proper_divisors) > number:
		return True

divisors_nums = []
abundant_numbers = []
abundant_numbers_sums = []

for i in range(1, 28124):
	if abundant_number(i):
		abundant_numbers.append(i)

for i in range(len(abundant_numbers)):
	for k in range(i, len(abundant_numbers)):
		if abundant_numbers[i]+abundant_numbers[k] <= 28123:
			abundant_numbers_sums.append(abundant_numbers[i]+abundant_numbers[k])


print((28123*28124*0.5)-sum(list(set(abundant_numbers_sums))))
