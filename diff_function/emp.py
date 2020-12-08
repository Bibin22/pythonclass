f = open('employee', 'r')
employee={}
lst = []
for lines in f:
    id, name, desig, exp, salary = lines.rstrip('\n').split(',')
    print(id, name, desig, salary)
    employee[id] = {'id':id, 'name': name, 'exp':exp,'salary':salary}
for k, v in employee.items():
    print(k, v)
def print_data(**kwargs):
    if 'id' in kwargs:
        id = kwargs['id']
        #print(id)
        print(employee[id]['name'])
print_data(id='1000')