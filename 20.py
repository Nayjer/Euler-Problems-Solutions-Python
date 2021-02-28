def factorial(n):
	fact = 1
	for i in range(1,n+1):
		fact = fact * i
	return fact

digit_sum = 0

for i in str(factorial(100)):
	digit_sum += int(i)

print(digit_sum)
