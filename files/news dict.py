f = open('data', 'r')
dict = {}
for lines in f:
    words = lines.rstrip('.\n').split(' ')
    #print(words)
    for word in words:
        if word not in dict:
            dict[word] = 1
        else:
            dict[word]+=1
print(dict)

lst = []
for values in dict.values():
    lst.append(values)
fq = max(lst)
print(fq)
for key, value in dict.items():
    if value == fq:
        print("most frequent word is: ", key)




high = max(dict, key =dict.get)
print(high)


