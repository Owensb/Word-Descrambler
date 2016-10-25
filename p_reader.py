#Thiis is a word descrambler for a word puzzle. We currently know there are probably two words, of length 10 and 11. 
# We have a few letters from each word and want to use a dictionary search to find them. 

#Variables for each possible word

#use python  p_reader.py < p.txt to input (p.txt can be any file input)
tens = []
elevens= []

#Variables to hold space for when we know a letter
elevens_known= []
tens_known = []

#Sort through the dictionary and get only the words of length 10 and 11
for i in range(0,  58110):
	word = input()
	if len(word) == 10:
		tens.append(word)
	elif len(word) == 11:
		elevens.append(word)
	else:
		pass

#Use known letters to sort through the remaining words

for i in range(0, len(elevens)):
	word=elevens[i]
	if('p' in word) & ('n' in word) & ('a' in word) & ('l' in word):
		elevens_known.append(elevens[i])
print(elevens_known)

for i in range(0, len(tens)):
	word=tens[i]
	word.count('p')
	if (word.count("p") >= 2) & ('c' in word):
		tens_known.append(tens[i])
#print(tens_known)
