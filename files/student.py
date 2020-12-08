f = open('student', 'r')
students = {}
for lines in f:
    id, name, course, total = lines.rstrip('\n').split(',')
    students[id] = {'id': id, 'name': name, 'course':course,'total':total }
print(students)

"""for k, v in students.items():
    print(k, v)
"""

def print_student(**kwargs):
    if 'id' in kwargs:
        rno = kwargs['id']
        if rno in students:
            print(students[rno]['name'])
            if 'property' in kwargs:
                prop = kwargs['property']
                if prop in students[rno]:
                    print(students[rno][prop])
                else:
                    print('invalid property')
    else:
        print('student does not exist')
id = input("enter id")
property = input("enter property")
print_student(id=id, property=property)



