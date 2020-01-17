def speak_excitedly(x, **kw):
	#print("x:", x)
	print("kw:",kw)
	times = kw['times']
	upper_case = kw['upper_case']
	if upper_case:
		x = x.upper()
		print(x, times * '!')
	else:
		print(x, times * '!')
	
	
if __name__ == '__main__':
	speak_excitedly("hello, world",**{"times":5, "upper_case":True})