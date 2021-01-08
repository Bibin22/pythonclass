class Employee:
    def __init__(self,id,name,exp,salary,desig):
        self.id = id
        self.name = name
        self.exp = exp
        self.salary = salary
        self.desig = desig
    def __str__(self):
        return self.name

    def display(self):
        print(self.id)
        print(self.name)
        print(self.exp)
        print(self.salary)
        print(self.desig)


f = open('employee', 'r')
lst=[]
objects = []
for lines in f:
    id, name, exp, salary, desig = lines.rstrip("\n").split(',')
    ob = Employee(id, name, exp, salary, desig)
   # ob.display()
    lst.append(ob)
for emp in lst:
    print(emp)
ename = list(map(lambda emp: emp.name.upper(), lst))
print(ename)
des = list(filter(lambda emp: emp.desig=='developer', lst))
for emp in des:
    print(emp)

sal = list(filter(lambda emp: int(emp.salary) > 23000, lst))
for emp in sal:
    print(emp.name, emp.desig, emp.salary)