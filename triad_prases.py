def check(user_input):
	phrase_words = user_input.split(" ")
	print(phrase_words)
	ans = []

	
	for word in phrase_words:
		w = []
		tri_words = []
		alternate_word1 = [] 
		alternate_word2 = []
		w.append(word)
		print(w)
		i = 1
		for j in word:
			if i % 2 == 0:
				alternate_word1.append(j)
			else:
				alternate_word2.append(j)
			i = i+1
		
		even_char_word = ''.join(alternate_word2)
		odd_char_word = ''.join(alternate_word1)
		#print(even_char_word, odd_char_word)
		tri_words.append(odd_char_word)
		tri_words.append(even_char_word)
		print('tri_words =' , tri_words)
		
		# check if the word is tri-word.
		'''
		
		read dict words from file
		if the tri_words is present in word file then true else false 
		'''
		dictionary_words_original = open("words", 'r').readlines()
		
		#dictionary_words_updated = []
		#for word in dictionary_words_original:
		#dictionary_words_updated.append(word.strip())
			
			
		dictionary_words_updated = [word.strip() for word in dictionary_words_original]
		
		#print(dictionary_words_updated[:10])
		for t_word in tri_words:
			if t_word in dictionary_words_updated:
				continue
			else:
				return False
		ans.append(True)

	for i in ans:
		if j:
			continue
		else:
			return False
	return True
				
			
			
		
	

if __name__ =='__main__':
	
	user_input = str(input("Enter the Phrase:	"	))
	result = check(user_input)
	print('Is it a triad phrase?: ', result)
	