#!/usr/bin/python3

"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
"""

pyramid = open("p067_triangle.txt", "r")
numbers = pyramid.read().split()

#didn't find for myself a good approach to solve that problem, i tried out 2 but they are too complicated, here's a good explanation for the easy way https://stackoverflow.com/questions/8002252/euler-project-18-approach/8002423#8002423

sep_sum = [int(numbers[i]) for i in range(int((100-1)*(100)/2),int((100*(100+1)/2)))] #at first i generate the last row of numbers, i use the gauß formula here to determine which index these numbers must have

for n in range(99,0,-1): #starting at the 99st row
	new_sep_sum = [] #because every turn the last sum-row gets 1 smaller, this will be my new each time
	for k in range(0,n):
		if sep_sum[k] >= sep_sum[k+1]: #check what way is better
			new_sep_sum.append(sep_sum[k]+int(numbers[int(n*(n-1)/2)+k]))	#for the higher number i can add this number and the adjacent number belonging to that two in the list
		else:
			new_sep_sum.append(sep_sum[k+1]+int(numbers[int(n*(n-1)/2)+k]))
	sep_sum = new_sep_sum #here we refresh the list

print(sep_sum[0]) #now the list has only 1 element, that will be the max output
