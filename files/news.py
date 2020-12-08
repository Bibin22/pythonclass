f1 = open('data', 'r')
lst =[]
for lines in f1:
    words = lines.split(' ')
    for word in words:
        lst.append(word.rstrip('.\n'))
print(lst)