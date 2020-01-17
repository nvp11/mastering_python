def gcd(a,b):
	print('(a,b)=',(a,b))
	 
	while b != 0:
		(a,b) = (b,a%b)
	return a 
	
	




if __name__ == '__main__':
	
	a, b = [int(x) for x in input("Enter the numbers:	").split()]
	#a, b = [input("Enter the numbers:	").split( )]
	result = gcd (a,b)
	print (result) 
	

