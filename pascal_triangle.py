'''
for each row

   print stars
   calculate remaining position
   print digits
   
'''

def calculate_pascal_row_from_previous_row(a_row):
	'''
	a_row = [] return [1]
	a_row = [1] return [1,1]
	input : a_row = [1,4,6,4,1] type(input) = <list> , integer
	output : pascal_row = [1,5,10,10,5,1] type(pascal_row) = <list>, integer
	
	input : a_row = [1,4,2,3,5,1]
	output : pascal_row = [1,5,6,5,8,6,1]
	'''
	
	pass

def pascal_triangle_no_space(user_input):
    pass

def traingle2(user_input):
	'''row_number = 1
	print('*' * (user_input-row_number), end= '')
	print('I' * row_number)
	
	row_number = 2
	print('*' * (user_input-row_number), end = '')
	print('I' * row_number)
	
	row_number = 3
	print('*' * (user_input-row_number), end = '')
	print('I' * row_number)'''
	
	for row_number in range(1,user_input+1,1): #[1,2,3]:
		print(' ' * (user_input-row_number), end = '')
		
		
		
		
		000000000001
		print(str(row_number) * row_number)


def triangle (i):
	
	for j in range (i+1):
		for k in range(j):
			print("*" * (i-k))
		print(j, end = " ")
		print("\n")
		
	
	
	'''for j in range(i+1):
		#print('* ' * (i-1))
		for k in range(j):	
			
			print ("*", end = " " )
			for t in reversed(range (i)):
				print(j, end = " ")
		print("\n")'''
			
	

if __name__ == '__main__':
	i = int(input("Enter number to form triangle:"))
	#triangle(i)
	traingle2(i)
	
	'''
	1
	22
	333
	4444
	55555
	
	1
	11
	121
	1331
	14641
	'''
	
	
	
	
	