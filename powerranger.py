
number = input("Enter number")
i = 1
total = 0
while(i<=int(number)):
    #print(number*i)
    data = number *i
    total = total + int(data)
    i+=1
print(total)