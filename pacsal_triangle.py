def triangle (i):
	
	for j in range(i+1):
		for k in range(j):	
			print(j, end = " ")
		print("\n")
			
	

if __name__ == '__main__':
	i = int(input("Enter number to form triangle:"))
	triangle(i)
	