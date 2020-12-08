text = "ABABAC"
dict = {}
"""for i in text:
    if i not in dict:
        dict[i] =1
    else:
        dict[i] += 1
print(dict)"""


for i in text:
    if i not in dict:

        dict[i] = 1
    else:
        print(i)
        break


