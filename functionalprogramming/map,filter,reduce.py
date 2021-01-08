lst = [10,11,12,13,14,15,2]
#map(function,iterable)

squre = list(map(lambda num:num**2, lst))
print('square', squre)
cubes = list(map(lambda num:num**3, lst))
print('cubes', cubes)


#filter

even = list(filter(lambda no: no%2==0, lst))
print('even', even)



#reduce
from functools import *
sum = reduce(lambda n1, n2: n1+n2, lst)
print(sum)

minimum = reduce(lambda n1, n2: n1 if n1<n2 else n2, lst)
print(minimum)

maximum = reduce(lambda n1, n2: n1 if n1>n2 else n2, lst)
print(maximum)

evenmin = reduce(lambda n1, n2: n1 if n1<n2 else n2, list(filter(lambda n: n%2 ==0, lst)))
print(evenmin)
