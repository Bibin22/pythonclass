class Person:
    def set_person(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def print_person(self):
        print('name', self.name)
        print('Age', self.age)
        print('Gender', self.gender)

name = input("enter a name")
age = int(input('Enter age'))
gender = input('Enter gender')
s = Person()


s.set_person(name,age,gender)
s.print_person()

obj1 = Person()
obj1.set_person('basil', 23, 'male')
obj1.print_person()
obj1.age+= 1
obj1.print_person()