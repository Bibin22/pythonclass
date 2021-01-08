from re import *
f = open('phone', 'r')
fout =open('validphone', 'w')
phoneno = set()
for phone in f:
    phoneno.add(phone.rstrip('\n'))
rule =
for numbers in phoneno:
    matcher = match(rule, numbers)
    if matcher != None:
        print(numbers, 'valid')
    else:
        print(numbers,"invalid")