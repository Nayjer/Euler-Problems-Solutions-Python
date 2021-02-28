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
