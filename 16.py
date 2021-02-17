"""
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 21000?
"""

number = 2**1000

def checksum(n):
	checksum = 0
	for i in str(n):
		checksum += int(i)
	return checksum

print(checksum(number))
