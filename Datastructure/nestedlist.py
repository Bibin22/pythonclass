student = [
    [100, 'abin', 'bca', 145],
    [101, 'bibin', 'mca', 155],
    [102, 'cibin', 'bca', 165],
    [103, 'dibin', 'mca', 175],
    [104, 'fibin', 'bcom', 185],

]

for students in student:
    print(students[1])
total = 0
for students in student:
    total = total + students[3]
print(total)

for students in student:
    if students[2] == "mca":

        print(students)
btotal = 0
mtotal = 0
bctotal = 0
for students in student:
    if students[2] == "mca":
        mtotal = mtotal + 1
    elif students[2] == "bca":
        btotal = btotal + 1

    elif students[2] == "bcom":
        bctotal = bctotal + 1




print("bca", btotal)
print("mca", mtotal)
print("bcom", bctotal)
