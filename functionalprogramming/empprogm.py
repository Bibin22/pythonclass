from functools import *
class Employee:
    def __init__(self,eid,ename,desig,salary,exp):
        self.eid = eid
        self.ename = ename
        self.desig = desig
        self.salary = salary
        self.exp = exp

    def __str__(self):
        return self.ename

f = open('emploee', 'r')
employee = []
for lines in f:
    eid, ename, desig, salary, exp = lines.rstrip('\n').split(',')
    employee.append(Employee(eid,ename,desig,salary,exp))
for emp in employee:
    print(emp)


"""hsalary = reduce(lambda s1,s2: s1 if s1>s2 else s2, list(map(lambda emp: emp.salary, employee)))
print(hsalary)
edetails = list(filter(lambda emp: emp.salary == hsalary, employee))
for emp in edetails:
    print(emp)"""

devsalary = reduce(lambda s1, s2: s1 if s1>s2 else s2,
                   list(map(lambda emp: emp.salary,
                            list(filter(lambda emp: emp.desig == 'developer', employee)))))
print(devsalary)



