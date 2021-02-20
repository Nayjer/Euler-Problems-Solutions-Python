#!/usr/bin/python3 

"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:
"""

pyramid = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

numbers = pyramid.split() #get the numbers in a list

combinations = []

for i in range(1,3): #if we start at the top, we allways need to decide if we go to the left adjacent element or to the right, that 14 times, so we need all these 2^14 combinations to brute force
	for k in range(1,3):
		for i1 in range(1,3):
			for k1 in range(1,3):
				for i2 in range(1,3):
					for k2 in range(1,3):
						for k3 in range(1,3):
							for k4 in range(1,3):
								for k5 in range(1,3):
									for k6 in range(1,3):
										for k7 in range(1,3):
											for k8 in range(1,3):
												for k9 in range(1,3):
													for k10 in range(1,3):
														combinations.append([i,k,i1,k1,i2,k2,k3,k4,k5,k6,k7,k8,k9,k10])		
path_sums = [] #here we save all path sums

def determine_next_element_1(index): #gets the left adjacent number
	for i in range(1, 15):
		if index in list(range(int((i-1)*(i)/2),int((i*(i+1)/2)+1))): #because in first row there is 1 element, in next 2, then 3, 4, 5 and so on, we can use the gauß formula to determine
			next_element_1 = index+i
	return next_element_1

def determine_next_element_2(index): #gets the right adjacent number
	for i in range(1, 15):
		if index in list(range(int((i-1)*(i)/2),int((i*(i+1)/2)+1))):
			next_element_2 = index+i+1
	return next_element_2


for combination in combinations:
	path_sum = 75 #thats the first number
	index = 0
	for way in combination: #if way = 1, we go to the left adjacent number
		if way == 1: 
			path_sum += int(numbers[determine_next_element_1(index)])
			index = determine_next_element_1(index)
		else:
			path_sum += int(numbers[determine_next_element_2(index)])
			index = determine_next_element_2(index)
	path_sums.append(path_sum)

print(max(path_sums))
