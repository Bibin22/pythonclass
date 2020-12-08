students={
    100:{'rol':100, 'name':'test1', 'course':'bca', 'total': 150},
    101:{'rol':101, 'name':'test2', 'course':'mca', 'total': 160},
    102:{'rol':102, 'name':'test3', 'course':'mca', 'total': 170}

}
for k, v in students.items():
    print(k, v)

""""def print_students(**kwargs):
    if 'id' in kwargs:

        rol = kwargs['id']
        if rol in students:
            print(students[rol]['name'])
            if 'property' in kwargs:
                prop = kwargs['property']
                if prop in students[rol]:
                    print(students[rol][prop])
                else:
                    print('invalid property')
    else:
        print('student doesnot exist')







id = int(input("enter id"))
property = input("enter property")
print_students(id=id, property=property)

"""