class Student:
    def __init__(self,roll, name, course, total):
        self.roll = roll
        self.name = name
        self.course = course
        self.total = total

    def print_student(self):
        print('roll no',self.roll)
        print('name',self.name)
        print('course', self.course)
        print('total', self.total)
roll = int(input('roll number'))
name = input('enter name')
course = input('Enter course')
total = int(input('enter total'))

ob=Student(roll,name,course,total)
ob.print_student()