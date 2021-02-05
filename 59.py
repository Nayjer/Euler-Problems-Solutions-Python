#!/usr/bin/python

"""
XOR decryption

Each character on a computer is assigned a unique code and the
preferred standard is ASCII (American Standard Code for
Information Interchange). For example, uppercase A = 65,
asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the
bytes to ASCII, then XOR each byte with a given value, taken
from a secret key. The advantage with the XOR function is that
using the same encryption key on the cipher text, restores the
plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the
plain text message, and the key is made up of random bytes. The
user would keep the encrypted message and the encryption key in
different locations, and without both "halves", it is impossible
to decrypt the message.

Unfortunately, this method is impractical for most users, so the
modified method is to use a password as a key. If the password
is shorter than the message, which is likely, the key is
repeated cyclically throughout the message. The balance for this
method is using a sufficiently long password key for security,
but short enough to be memorable.

Your task has been made easy, as the encryption key consists of
three lower case characters. Using p059_cipher.txt (right click
and 'Save Link/Target As...'), a file containing the encrypted
ASCII codes, and the knowledge that the plain text must contain
common English words, decrypt the message and find the sum of
the ASCII values in the original text.
"""

chars = open("p059_cipher.txt", "r")
text = chars.read()
char_list = text.split(",")

possible_keys = [] #[a-z][a-z][a-z] to number values "[97-122][97-122][97-122]"

for i in range(97,122):
	for k in range(97,122):
		for z in range(97,122):
			possible_keys.append(str(i)+","+str(k)+","+str(z)) #generates all possible_keys

decrypted_chars = [] #all decrypted chars of the cipher.txt with all possible keys (26^3)

for i in possible_keys:
	decrypted_char = []
	values = i.split(",")
	for k in range(0,len(char_list),3): #each chraracter of key gets XOR'd with 1 ASCII value. so we decrypt it
			decrypted_char.append(int(char_list[k])^int(values[0]))
			decrypted_char.append(int(char_list[k+1])^int(values[1]))
			decrypted_char.append(int(char_list[k+2])^int(values[2]))
	decrypted_chars.append(decrypted_char) #append these decrypted chars as a list to a bigger list, so we can seperate them

counts = []

for i in decrypted_chars: #this loop counts the number of english-letters for each decrypted text
	count = 0
	for k in i:
		if 32 <= int(k) <= 90 or 97 <= int(k) <= 122:
			count += 1
	counts.append(count)

	
for i in range(len(counts)): #the decrypted text with the biggest count needs to be the right decrypted text
	if counts[i] == max(counts):
		print(i)

number = 0

for i in decrypted_chars[3090]: #3090 is what i printed out in the upper loop
	number += int(i)

print(number)
