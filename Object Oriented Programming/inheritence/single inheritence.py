class Parent:
    def f1(self):
        print('parent')

class Child(Parent):
    def f2(self):
        print('child')


o = Child()
o.f1()
o.f2()