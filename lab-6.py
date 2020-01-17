def cyclone_phrase(i):
	
	words = i.split(" ")
	print ('w =',words)
	word_answers = []
	
	for word in words:
		values = []
		diff = []
		ans = []
		length = len(word)
		print('length of word', length)
		len_of_word = int(length/2)
		#print (len_of_word)
		
		for j in word: 
			k = ord(j)
			values.append(k)
		print ('Values = ',values)
		r = True
		
		for i in range(len_of_word):
			if values[i] - values[length-1-i]<=0:
				continue
			else: 
				r = False
		
		for i in range(len_of_word):
			if values[length-1] - values[i+1] <= 0:
				continue
			else:
				r = False
		if r == True:
			ans.append(True)
		else:
			ans.append(False)
			
	for j in ans:
		if j:
			continue
		else: 
			return False
	return True
	
if __name__== '__main__':

	i = str(input("Enter Phrase:  ")).strip()
	result = cyclone_phrase(i)
	print('Result:   ',result)