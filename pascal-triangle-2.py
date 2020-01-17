def calculate_pascal_row_from_previous_row(a_row):
	#print (a_row)
	'''input_row = []
	for i in a_row:
		input_row.append(int(i))'''
	
	
	output_sum = []
	input_row = []
	input_row.append(int(1)) #[1]
	
	#for k in range(1):
	print(" " * ((a_row)-len(output_sum)-1), end = " " )
	print(" ".join([str(x) for x in input_row]))
	input_row.append(int(1)) # [1,1]
	#for k in range(1):
	print(" " * ((a_row)-len(output_sum)-2), end = " " )
	print(" ".join([str(x) for x in input_row]))
			
	output = []
	ans = 0
		
	#print('Input:	', input_row)
	
	'''if input_row == []:
		return ([1])
	elif input_row == [1]:
		return ([1,1])'''
		
		
	'''for j in range(a_row-2):
			
		for i in range(len(input_row)-1):
			
			ans = input_row[i]+ input_row[i+1]
			#print(int(i))
			#print(int(i+1))
			#print ('a:	', ans)
			output_sum.append(ans)
		output_sum.insert(0, int("1"))
		output_sum.append(1)
			#print('1', output_sum, '1')
		
		print(output_sum)
		
	
		input_row = output_sum
		output_sum = []
		#print('input', input_row)'''
		
		
	for j in range(a_row-2):
			
		for i in range(len(input_row)-1):
			
			ans = input_row[i]+ input_row[i+1]
			'''print(int(i))
			print(int(i+1))
			print ('a:	', ans)'''
			output_sum.append(ans)
		output_sum.insert(0, int("1"))
		output_sum.append(1)
				#print('1', output_sum, '1')
		
		for k in range(1):
			print(" " * ((a_row)-len(output_sum)), end = " " )
			print( " ".join([str(x)for x in output_sum])) 
			
				
	
		input_row = output_sum
		output_sum = []
		#print('input', input_row)
	
	'''
	a_row = [] return [1]
	a_row = [1] return [1,1]
	input : a_row = [1,4,6,4,1] type(input) = <list> , integer
	output : pascal_row = [1,5,10,10,5,1] type(pascal_row) = <list>, integer
	
	input : a_row = [1,4,2,3,5,1]
	output : pascal_row = [1,5,6,5,8,6,1]
	'''
	

	
if __name__ =='__main__':
	#a_row = list(input("Enter the list:	"))
	a_row = int(input("Enter the list:	"))
	result = calculate_pascal_row_from_previous_row(a_row)
	

	