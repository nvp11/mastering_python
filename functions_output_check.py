'''def all_together(x, y, z=1, *nums, indent=True, spaces=4, **options):
 
	print("x:", x)
	print("y:", y)
	print("z:", z)
	print("nums:", nums)
	print("indent:", indent)
	print("spaces:", spaces)
	print("options:", options)

	
if __name__ == '__main__':

	#all_together(2)
	#all_together(2, 5, 7, 8, indent=False)
	#all_together(2, 5, 7, 6, indent=None)
	#all_together()
	#all_together(indent=True, 3, 4, 5)
	#all_together(**{'indent': False}, scope='maximum')
	#all_together(dict(x=0, y=1), *range(10))
	#all_together(**dict(x=0, y=1), *range(10))
	#all_together(*range(10), **dict(x=0, y=1))
	#all_together([1, 2], {3:4})
	#all_together(8, 9, 10, *[2, 4, 6], x=7, spaces=0, **{'a':5, 'b':'x'})
	#all_together(8, 9, 10, *[2, 4, 6], spaces=0, **{'a':[4,5], 'b':'x'})
	all_together(8, 9, *[2, 4, 6], *dict(z=1), spaces=0, **{'a':[4,5], 'b':'x'})'''
	
	
'''def say_hello():
	print("Hello!")
print(say_hello())

def echo(arg=None):
    print("arg:", arg)
    return arg

print(echo())  # => ?
print(echo(5)) # => ?
print(echo("Hello")) # => ?

def drive(has_car):
    if not has_car:
        # Please never actually signal an error like this
        return "Oh no!"
    return 100  # miles

print(drive(False))  # => 
print(drive(True))   # => ?'''


def reassign(arr):
	print("Before assign = {}".format(arr))
	arr = [4, 1]
	print("Inside reassign: arr = {}".format(arr))

def append_one(arr):
    arr.append(1) 
    print("Inside append_one: arr = {}".format(arr))

l = [4]
print("Before reassign: arr={}".format(l))  # => ?
reassign(l)
print("After reassign: arr={}".format(l))  # => ?

l = [4]
print("Before append_one: arr={}".format(l))  # => ?
append_one(l)
print("After append_one: arr={}".format(l))  # => ?


# Case 1
x = 10

def foo():
    print("(inside foo) x:", x)
    y = 5
    print('value:', x * y)

print("(outside foo) x:", x)
foo()
print("(after foo) x:", x)

# Case 2
x = 10

def foo():
    x = 8  # Only added this line - everything else is the same
    print("(inside foo) x:", x)
    y = 5
    print('value:', x * y)

print("(outside foo) x:", x)
foo()
print("(after foo) x:", x)


x = 10

def foo():
    print("(inside foo) x:", x)  # We swapped this line
    #x = 8                        # with this one
    y = 5
    print('value:', x * y)

print("(outside foo) x:", x)
foo()
print("(after foo) x:", x)
	
	
lst = [1,2,3]

def foo():

	print(lst)
	lst.append(4)
foo()

lst = [1,2,3]
def foo():
	print(lst, lst + [4])
	#lst = lst + [4]
foo()