name = ['a', 'b', 'c', 'd', 'e', 'f']
pas = ['a', 'b', 'c']

st1 = set(name)
st2 = set(pas)
fail = st1.difference(st2)
print(fail)