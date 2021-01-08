import re
matcher = re.finditer('ab','ababababababababababababababababababababababababab')
count = 0
for match in matcher:
    print(match.start())
    #print(match.group())
    count+=1
print('how many ab ', count)

