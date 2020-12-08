#step1 create file refference
f = open("txt", "r")
lst =[]
"""for lines in f:
    print(lines)"""

"""for lines in f:
    lst.append(lines)
print(lst)"""

st = {}
for lines in f:
    lst.append(lines.rstrip("\n"))
    st = set(lst)
print(st)


