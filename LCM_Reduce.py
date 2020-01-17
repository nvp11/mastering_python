import operator
import functools
import operator
from functools import reduce
from fractions import gcd

'''def lcm(*nums):
   functools.reduce(lambda x,y: [(x*y)// gcd(x,y)],[1,1,1,1])
    

lcm()'''


def fact(n):
	functools.reduce([lambda x : operator.mul(range(1,n+1))],range(1,n+1))
	
fact(n=10)