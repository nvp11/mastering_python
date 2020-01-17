def triangle (i):
	#for t in range(i):
		for j in reversed(range(i+1)[1:]):
			for k in range(j):	
				print (" ", end = " " )
			
			
			# print digit 
			for t in range(i-k):
				print(j, end = " ")
			print("\n")
				
		

if __name__ == '__main__':
	i = int(input("Enter number to form triangle:"))
	triangle(i)
	
'''
****
***
**
*

1
22
333
4444
55555


****1
***22
**333
*4444
55555
'''

'''
1

'''