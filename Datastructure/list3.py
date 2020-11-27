lst = [9, 8, 7, 6, 4, 3, 2]
lst1 =[]
for i in lst:
    if i > 5 :
        lst1.append(i+1)
    else:
        lst1.append(i-1)
print(lst1)
