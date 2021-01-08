from re import *
rule = '[a-kA-K][369][a-zA-Z0-9]*'
variablename = input('enter vaeiable name')
matcher = fullmatch(rule, variablename)
if matcher!=None:
    print('valid variable name')
else:
    print('invalid')