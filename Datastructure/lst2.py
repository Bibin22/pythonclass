l = int(input("Enter a limit"))
lst = []
for i in range(1,l+1):
    lst.append(i)
print(lst)
odd =[]
even =[]
for i in lst:
    if i %2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(odd)
print(even)