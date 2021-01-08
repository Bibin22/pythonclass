first = [1,2,3]
second = [4,5,6]
"""
for i in first:
    for j in second:
        print((i, j))"""

pairs = [(i, j) for i in first for j in second]
print(pairs)

squrese = [ i**2 for i in first]
print(squrese)

sq = [[i**2 for i in first], [j **2 for  j in second] ]
print(sq)
# print((i, j) for i in first for j in second)

third = [1,2,3,4,5,6,7]
data = [i-1 if i<5 else i+1 for i in third]
print(data)

fourth = [1,2,3,4,5,6,7,8]
data1 = [i+1 if i>5 else i-1 if i<5 else 5 for i in fourth]
print(data1)

fifth = [1,2,3,4,5,6,7,8,5,0]
data2 = [i+1 if i>5 else i-1 if i<5 else 0 if i==0 else 1 for i in fifth]
print(data2)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
flat = [j for i in matrix for j in i]
print(flat)