print('this program is to practice FAR')

def getMachineIP_and_network(ipaddress_str):
    # example ipaddress 192.2.3.5/20
    # print the ipaddress
	# get the subnet mask and get its datatype
	# get the ip address and get its datatype
	# cnvert the ipaddress to binary format
	# convert the subnet mask to binary format
	# get network ip
	# return both machine ip and network ip
	
	print (ipaddress_str)
	ipaddress = ipaddress_str[0:12]
	print ('ipaddess =', ipaddress)
	subnet = int(ipaddress_str[13:15])
	print ('subnet =', subnet)
	print(type (ipaddress))
	print(type(subnet))
	values = ipaddress.split(".")
	print(values)
	
	number = []
	number_binary =[] 
	for i in values:
	  number.append(int(i))
	  number_binary.append("{0:08b}".format((int (i))))
	print('Number = ', number)
	print('Binary = ', number_binary)
	
	
	number_int = [] 
	dec = []
	dec_int = []
	ip_address = [] 
	for i in number_binary:
		number_int.append(int(i))
		dec.append(format(int(i,2)))
	for i in dec:
		dec_int.append(int(i))
	for i in dec: 
		
		ip_address = ".".join(dec)
	
	ip_mask = ip_address + "/" + str(subnet) 
		
	
	print('Converted to int = ', number_int)
	print('decimal = ', dec)
	print('dec_int =', dec_int)
	print ('ipaddress = ' , ip_address) 
	print('ip_mask = ' , ip_mask)
	
	
	
	
		
	
	
	
if __name__ == '__main__':
   ipaddress_str = "192.168.1.27/20"
   
   getMachineIP_and_network(ipaddress_str)
 
   



