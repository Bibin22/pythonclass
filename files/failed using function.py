f1 = open('names', 'r')
f2 = open('pass', 'r')

def convert_to_set(file):
    file_set = set()
    for lines in file:
        file_set.add(lines.rstrip('\n'))
    return file_set

nameset = convert_to_set(f1)
passset = convert_to_set(f2)
result = nameset - passset
print(nameset)
print(passset)
print(result)