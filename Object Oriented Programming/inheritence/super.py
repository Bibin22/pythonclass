class Parent:
    def __init__(self, name, clas):
        self.name = name
        self.clas = clas
    def display_student(self):
        print('name', self.name)
        print('class', self.clas)
class Children:
    def __init__(self, total):
        self.total = total

    def display_total(self):
        print('total', self.total)


class Subchild(Parent, Children):
    def __init__(self, teacher):
        self.teacher = teacher
        #super(Subchild, self).__init__('bibin', 'mca')
        super(Subchild, self).__init__(120)
    def print(self):
        print('teacher', self.teacher)



ob = Subchild('bbbbb')

ob.display_total()
ob.print()



ob = Children(120)
ob.display_total()
ob.display_student()

