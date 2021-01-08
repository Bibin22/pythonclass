f = open('employee')
for lines in f:
    data= lines.rstrip('\n').split(',')
    print(data)