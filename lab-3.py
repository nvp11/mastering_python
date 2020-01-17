# Fahrenheit to Celsius converter 


def F_to_C(i):
	
	c = round((i - 32)*(5/9), 2)
	print('Temprature in Celsius:', c)
	
if __name__== '__main__':

	i = int(input("Enter Temp in Fahrenheit: "))

	F_to_C (i)