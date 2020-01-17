
def flip_dict(dict):
	flipped_dict = {}
	for i in dict:
		value = dict[i]
		print(i,value)
		
		
		if flipped_dict.get(value, None) == None:
			flipped_dict[value] = []
		
		flipped_dict[value].append(i)
		   
		#flipped_dict[value] = i
	print('flipped dict =' , flipped_dict)


'''
key1
'''


if __name__ == '__main__':
	user_input = {}
	usr = input('key,value =')
	
	while usr != '-1':
	  print(usr)
	  key,value = usr.split(",")
	  user_input[key] = value
	  usr = input('key,value =')
	 
	print(user_input)
	flip_dict(user_input)
	