from re import *
#pattern = '[a-z]' #small leter a-z
#pattern = '[0-9]' #0 t0 9
#pattern = '[^0-9]' # remove numbers
#pattern = '[^a-z]' # remove small leter a-z
#pattern = '[a-zA-Z]' # small leter a-z capital leteers AtoZ
#pattern = '[a-zA-Z0-9]'
#pattern = '[^ a-zA-Z0-9]'
#pattern = "\s" #checking for space
#pattern = "\S" #except space
#pattern = "\d" #for digits
#pattern = "\D" #except digit
#pattern = "\w" #except special charectors
pattern = "\W" #include special Charectors

matcher = finditer(pattern, 'abc Z@7k')
for match in matcher:
   # print(match.start())
    print(match.group())

"""out = [(match.start(), match.group()) for match in matcher]
print(out)"""