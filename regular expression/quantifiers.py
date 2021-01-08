from re import *
#pattern = "a+" #check for a and morethan one a
#pattern = 'a*' # a+ plus and zero occurance of a
#pattern = 'a?' #checking for a and zero occurance
pattern = '^a' #check for startung with a
#pattern = 'a$' # check for ending with a
#pattern = 'a{2,3}' #checking for 2 a maximum 3a
"""mather = finditer(pattern,'aaaaababababaaaa')
for match in mather:
    print(match.start())
    print(match.group())"""

matcher = fullmatch(pattern,'aaaaababababaaaa')
if matcher !=None:
    print('given string starting with a')
else:
    print('given string not starting with a')