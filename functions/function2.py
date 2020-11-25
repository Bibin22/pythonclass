def add(a, b):
    c = a + b
    return c



def evencheck(num1):
    if num1 % 2 == 0:
        return "even"
    else:
        return "odd"
data = add(10, 5)
print(evencheck(data))