employee = [
    [1001, 'abin', 'qa', 1981, 2003],
    [1002, 'bibin', 'developer', 1992, 2008],
    [1003, 'cibin', 'ba', 1989, 2010],
    [1004, 'dibin', 'developer', 2009, 2014],
    [1004, 'fibin', 'developer', 1987, 1989],


]

for emp in employee:
    print(emp[1], "designation:", emp[2])
for emp in employee:
    if emp[2] == 'developer':
        print(emp[1], emp[2])
for emp in employee:
    if emp[3] > 1980 and emp[3] < 1990:
        print(emp[1], emp[3], emp[4])


for emp in employee:
    exp = emp[4] - emp[3]
    if exp > 9:
        print(emp[1], exp)

