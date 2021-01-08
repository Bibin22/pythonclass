f = lambda no1, no2:no1 + no2
print('sum =',f(10,20))

s = lambda n1, n2 :n1 - n2
print('sub =',s(90,89))

c = lambda n: n**3
print('cube =',c(200))

odd = lambda num:num % 2 !=0
print('odd or even',odd(20))

mul = lambda num1, num2 : num1 * num2
print('mul =',mul(5, 5))



upper = lambda name:name.upper()
print(upper('bibin'))




employee = ['ajay', 'viajay', 'anil', 'danie','tom', 'joy']
upper = list(map(lambda name: name.upper(), employee))
print(upper)

startswithA = list(filter(lambda name: name[0] == 'a', employee))
print(startswithA)