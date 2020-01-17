'''
what we learned:
	1. when to use [ and when to use (
	2. when to use "for" and when to use "while" both could be used but one would be easy to use compared to another
	3. how to read user input and convert to integer
	4. how to get input from system argument (to automate at scale) and what module to use (here its import sys)
'''
import sys

def collatz_seq(i):
	m = [i]
	
	for j in m:
		if i == 1:
			print('Collatz sequence = ',m)
			break
		else:
			if i % 2 == 0:
				i = i/2
			else:
				i = (i*3)+1
		m.append(i)
	print('Length of sequence = ',len(m))
	
	# 2nd METHOD
	
def coll_s(numb):
	
	seq = [numb] 
	
	while numb != 1:
		if numb % 2 == 0: 
			numb = numb/2 
		else:
			numb = (numb * 3) + 1
		seq.append (numb)
	print ('Collatz sequence = ',seq)
	print('Length of sequence = ',len(seq))
	
	
		
if __name__== '__main__':

	# no need for import sys
	i = int(input("Enter number : "))
	
	# system argument (requires to use statement import sys)
	argument = int(sys.argv[1])
	collatz_seq(argument)
	coll_s(13)
	
	
