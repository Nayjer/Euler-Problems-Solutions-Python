#!/usr/bin/python

"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

for i in range(1,1001):
	for k in range(1,1001):
		for z in range(1,1001):
			if i+k+z == 1000 and i**2+k**2==z**2: #because the sum of a, b, and c is 1000, the individual numbers need to be in the range from 1 to 1000, if the sum is 1000 and its a pythagorean triple, we have our number
				print(str(i)+","+str(k)+","+str(z))
				exit()
