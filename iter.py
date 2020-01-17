import itertools
import operator

for el in itertools.permutations('XKCD', 2):
    print(el, end=', ')

'''for el in itertools.cycle('LO'):
    print(el, end='')  # Don't run this one. Why not?'''

itertools.starmap(operator.mul, itertools.zip_longest([3,5,7],[2,3], fillvalue=1))

def dot_product(u,v):
	print(list(map(lambda x: sum(x[0]*x[1]), zip(u,v))))
dot_product([1, 3, 5], [2, 4, 6])
	
