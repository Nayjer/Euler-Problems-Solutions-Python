"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

def get_proper_divisor_sum(n):
	divs = []
	for i in range(1, n):
		if n % i == 0:
			divs.append(i)
	return [n, sum(divs)]

nums = []
adjacent_numbers = []

for i in range(1,10000):
	nums.append(get_proper_divisor_sum(i))

for i in range(len(nums)):
	for k in range(i+1,len(nums)):
		if nums[i][0] == nums[k][1] and nums[i][1] == nums[k][0]:
			adjacent_numbers.append(nums[i][0])
			adjacent_numbers.append(nums[k][0])			

print(sum(list(set(adjacent_numbers))))
