"""age = int(input('enter a age'))
if age< 18:
    raise Exception('invalid age')"""

num = input('enter a number')
if type(num)!='int':
    raise Exception('only intiger')