def average(*num):
	if len(num) == 0:
		print('Average:', None)
	else:	
		print('Average:', (sum(num))/len(num))
	
if __name__ == '__main__':

	average(5)
	average(8,6,9,11)
	average()
	