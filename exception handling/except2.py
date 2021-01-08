no1 = int(input("Enter  number"))
no2 = int(input("enter a number"))
try:
    res = no1/no2
    print(res)
except:
    no2 = int(input('Enter another value for no2'))
    try:
        res = no1/no2
        print(res)
    except:
        no2 = int(input('enter another number for m02'))
        try:
            res = no1/no2
            print(res)
        except:
            print('something wrong')
finally:
    print('final statement')