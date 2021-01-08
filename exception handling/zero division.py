no1 = int(input('Enter a number'))
no2 = int(input('enter a number'))
lst = [1,2,4]
try:
    res = no1/no2
    print(res)
except Exception as e:
    print(e.args)
try:
    print(lst[5])
except Exception as e:
    print(e.args)
