def sum_of_mul (result):
 
	max = 41
	numb = []
	 
	
	for i in range(41):
		if i % 3 == 0 or i % 5 == 0: 
			result = result + i 
	
	print(result)
	
	# 2nd METHOD 
	
	for i in range(1,42):
		if  i * 3 < max: 
			numb.append(i*3) 
	
	for i in range(1,42):
		if i * 5 < max:
			numb.append(i*5)
			
	numb = set(numb)
	numb = list(numb)
	print(numb)
	
	result = 0 # need to reset the value from previous usage
	
	for i in numb:
		result = result + i 
		
	print(result)
	print('Using sum function', sum(numb))
	'''
	results are not same 
	some error in addition 
	
	this for loop for addition works with boyh - set and list ? 
	yes for loop needs something that is iteratable i.e set, list, tuple, dictionary. all this should be fine. wanna learn a shortcut to add?
	sum(numb) is the shortcut
	okay .. was it a syntax error? any idea else leave it we can come back to it later.
	
	The "sum" is a function hence it takes "(" brakets you provided "[" which confuses interpreter and hence error. 
	
	how its time to push the code to git :-) okay 
	
	step 1 - place file in the git folder on local machine
	step 2 - check the status with "git status" (without quotes)
	step 3 - git add <filenames>
	step 4 - git commit -m <useful message for reference in future>
	step 5 - git push origin master
	  
	'''
	
			

	
	
			
	





if __name__== '__main__':
	
	sum_of_mul(result=0)

	