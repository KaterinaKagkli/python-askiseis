words = raw_input("Words: ")
wordlist = words.split(" ")
length = len(wordlist)
maxword = max(wordlist, key=len)

for i in range(length):
	if len(wordlist[i]) == len(maxword):
		maxword = wordlist[i]
		

print("Longest word: " + maxword)


	