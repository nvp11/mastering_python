'''
1) length of phrase 
2) if length = 1 or o ---> true 
3) else: 
4) finding values of phrase and saving in list 
5) finding the diff of that list and saving it to another list 
5) finding if the  final list is sorted or not
6) if yes then true
7) if no then false

'''

def surpassing_phrase (user_string):
	
	length = len(i) 
	print ('Length of phrase: ' , length) 
	
	if length == 1 or length == 0:
		print ('TRUE')
	else: 
		
		words = user_string.split(" ")
		print(words)
		word_answers = []
		for word in words: # for word in ["nidhi", "vakil"] 
			values = []
			diff =[]
		
			for j in word: # for j in ['n', 'i', 'd', 'h', 'i']
				k = ord(j)
				values.append (k)

			print ('Values = ',values)
		
		
			for j in range(len(word) - 1): 		
				d = abs(values[j] - values[j+1])
				diff.append (d) 
			
			print (word, 'diff =', diff)
		
			if sorted(diff) == diff:
				word_answers.append (True)
			else:
				word_answers.append (False)
				
		for j in word_answers:
			if j:
				continue
			else:
				return False
				
		return True
				
				
		
		
		'''for j in range(len(diff) - 1):
			if ( diff[j+1] - diff[j] ) > 0:
				continue
			else:
				print ('FALSE')
				break
		'''
			




if __name__== '__main__':

	i = str(input("Enter Phrase:  ")).strip()
	final_result = surpassing_phrase(i)
	print(final_result)

	