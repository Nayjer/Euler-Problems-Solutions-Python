def day_difference(year, month):
	diff = 359
	for i in range(1901, year):
		if i % 4 and not (i % 400 != 0 or i % 100 == 0):
			diff += 366
		elif i % 4 and not i % 400 == 0 and i % 100 == 0:
			diff += 365
		elif i == 2000:
			diff += 366
		else:
			diff += 365

	for i in range(1, month):
		if i == 4 or i == 6 or i == 8:
			diff += 30
		elif i == 2 and year % 4 == 0:
			diff += 29
		elif i == 2 and not year % 4 == 0:
			diff += 28
		else:
				diff += 31
	return diff
		
def is_sunday(year, month):
	if day_difference(year, month) % 7 == 0:
		return True

sundays = 0

for i in range(1901, 2001):
	for k in range(1,13):
		if is_sunday(i, k):
			sundays += 1

print(sundays-1)
