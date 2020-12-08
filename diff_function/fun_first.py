"""def add(n1, n2):
    res = n1 + n2
    print(res)
add(10, 20)"""



"""def add(*num):
    print(num)
    sum = 0 
    for i in num:
        sum = sum + i
    print(sum)

add(19, 20, 39, 45)"""

def print_data(**kwargs):
    print(kwargs)
    for k,v in kwargs.items():
        print(k,v)
print_data(birthplace ='kochi', desig= 'devop', salary=2500, wplace='aluva')