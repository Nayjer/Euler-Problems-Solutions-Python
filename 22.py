"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

native_names = open("p022_names.txt","r").read() #get names as a string, but unfortunately they have included a "" each
string_names = native_names.replace('"', '') #remove that "
names = string_names.replace(",", " ") #remove commas to sort the strings

sorted_names = [name.lower() for name in names.split()] #lower each name and append the names as strings each a list
sorted_names.sort() #sort the names in alphabetical value

scores = [] #here we save each score

for i in range(len(sorted_names)): #for each name
	score = 0
	for k in sorted_names[i]: #for each character
		score += ord(k)-96 #alphabetical value is the ASCII-Value minus 96
	score = score * (i+1) #at the end we multiplie all these alphabetical values of the name with the name position
	scores.append(score) #append it to the score list

print(sum(scores)) #the sum of the scores
