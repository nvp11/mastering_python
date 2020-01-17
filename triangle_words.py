
# Triange Numbers 

def triangle_numbers(i):
	seq = []
	n = 1
	words = i.split(" ")
	input_lenght = len(i)
	while n != input_lenght*27:
		k = int((n *(n+1)/2))
		seq.append (k)
		n = n+1
	print ('Sequence is: ', seq)
	
	for word in words:
		values = []
		ans = []
		add = 0
		
		for j in word: 
			values.append(ord(j)-64)
		print('Values: ',values)
		
		word_value = sum(values)
		print('Word_value = ', word_value)
		# search if the added_value is in the list of triangle numbers
		
		'''
		if word_value in seq:
			ans.append(True)
		else:
			ans.append(False)
		''' 
		for j in "nidhi":
			print(j)
		for j in seq: # j in seq means j takes value [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66] each value at a time. so j=1, j=3, j=6, ...
			if j == word_value:
				ans.append(True)
				
			else: 
				pass
			
				
	for j in ans:
		if j:
			continue
		else: 
			return False
	
	if len(ans) == 0:
		return False
	else:
		return True
			
			

if __name__ == '__main__':
	i = input(str("Enter Phrase:")).strip()
	triangle_numbers(i)
	result  = triangle_numbers (i)
	print ('Result = '  , result)
	