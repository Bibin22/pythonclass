f1 = open('names', 'r')
f2 = open ('pass', 'r')

st1 = set()




for lines in f1:
    st1.add(lines.rstrip("\n"))

print(st1)

st2= set()



for lines in f2:
    st2.add(lines.rstrip("\n"))

print(st2)


fail = st1.difference(st2)
print(fail)