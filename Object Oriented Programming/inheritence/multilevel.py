class Parent:
    def f1(self):
        print('parent')

class Child(Parent):
    def f2(self):
        print('Child')


class Subchild(Child):
    def f3(self):
        print('sub class')


ob = Subchild()
ob.f1()
ob.f2()
ob.f3()