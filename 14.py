lenghts = []

for i in range(2, 1000000):
	lenght = 1
	while i != 1:
		if i % 2 == 0:
			lenght += 1
			i = int(i*0.5)
		elif i % 2 != 0:
			lenght += 1
			i = 3*i+1
	print(lenght)
	lenghts.append(lenght)

print(max(lenghts))

index = lenghts.index(max(lenghts))
print(index)
