from re import *
f = open('vehiclenumbers', 'r')
fout =open('valid', 'w')
regno = set()
for numbers in f:
    regno.add(numbers.rstrip('\n'))
rule = 'KL\d{2}[A-Z]{1,2}\d{1,4}'
for vehiclenumber in regno:
    matcher = fullmatch(rule, vehiclenumber)
    if matcher != None:
        fout.write(vehiclenumber + "\n")
    else:
        pass