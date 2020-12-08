text = "hai how are you hai how are you"
dict = {}
words = text.split(' ')
print(words)
for word in words:
    if word not in dict:
        dict[word] =1
    else:
        dict[word]+= 1
print(dict)