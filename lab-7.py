
# Triange Numbers 

def triangle_numbers(i):
	seq = []
	n = 1
	while n != 27:
		k = int((n *(n+1)/2))
		seq.append (k)
		n = n+1
	print ('Sequence is: ', seq)
	
		
		
		



if __name__ == '__main__':
	i = input(str("Enter Phrase:")).strip()
	triangle_numbers(i)
	#result  = triangle_numbers (i)
	#print ('Result = '  , result)
	