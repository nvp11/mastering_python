def variadic(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

variadic(2, 3, 5, 7)
variadic(1, 1, n=1)
#variadic(n=1, 2, 3)
variadic()
variadic(cs="Computer Science", pd="Product Design")
#variadic(cs="Computer Science", cs="CompSci", cs="CS")
variadic(5, 8, k=1, swap=2)
variadic(8, *[3, 4, 5], k=1, **{'a':5, 'b':'x'})
variadic(*[8, 3], *[4, 5], k=1, **{'a':5, 'b':'x'})
variadic(*[3, 4, 5], 8, *(4, 1), k=1, **{'a':5, 'b':'x'})
variable_somename = {'a':5, 'b':'x'}
variadic(variable_somename, *{'a':6, 'b':'y'}, **{'a':5, 'b':'x'})

def default_value_function(

def power_2(val):
	result = val ** 2
	return result
	
lambda val: val ** 2

def multiply(x,y):
    result = x * y
	return result
	
(lambda x,y: x * y)(4,5) 

	