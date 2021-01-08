from re import *
rule = 'KL\d{2}[A-Z]{1,2}\d{1,4}'
vehiclenumber = input('enter vaeiable name')
matcher = fullmatch(rule, vehiclenumber)
if matcher!=None:
    print('valid vehicle  number')
else:
    print('invalid')
