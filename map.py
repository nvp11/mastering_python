print(list(map(int, ['12', '-1', '0'])))
print(list(map(len, ['hello','world'])))
print(list(map(lambda x:x[::-1],['hello','world'])))

#(lambda ...)(4)
#print([(lambda x:[x**1, x**2, x**3])(i) for i in range(2,6)])
print(list(map((lambda x:[x**1, x**2, x**3]), range(2,6))))
print(list(map((lambda x:[x**i for i in range(1,4)]), range(2,6))))


#print(list(lambda x:x**i for i range(1,4)) for i in range(1,4)))

#print(list(map(, [range(2,6)])))
#print(list(map(lambda x: zip(x), (range(2,5),range(3,9,2)))))

print(list(filter(lambda x:x>=0, [12,-2,0])))

for x,y in zip([2,3,4], [3,5,7]):
   print(x * y)
   
print([x*y for x, y in zip(range(2,5), range(3,9,2))])

print(list(map(lambda x:x[0]*x[1], zip(range(2,5), range(3,9,2)))))

'''

print(list(filter(lambda x: [x[i] for i in range(1,2)],['hello','world'])))

print(list(filter(lambda x: x[1],['hello','world'])))'''

print(list(filter(lambda x: x=='world',['hello','world'])))
print(list(filter(lambda x: x=='Stanford',['Stanford','Cal','UCLA'])))


'''
def multiple_3_filter(n):
   for i in range(20):
      if i % 3 ==0:
	     print(i)
'''		 
		 
print(list(filter(lambda x:x%3 == 0 or x%5 ==0 ,  range(20))))

score = ""

print((score == 1 and "winner" or (score == -1 and "loser") or ("tied")))

'''
def multiple_3(n):
   max_quotiant = n/3
   for i in range(max_quotiant+1):
     print(i*3)
	 
   multiple = 0
   counter = 0
   while multiple <n:
      print(multiple)
	  counter = counter + 1
	  multiple = counter * 3
'''	  


it = iter(range(100))
print(67 in it)  # => True
print(next(it))  # => ??
print(37 in it)  # => ??
print(next(it))  # => ??






























