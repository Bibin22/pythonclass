from dbconnection.dbconnect import *
db = get_connect()
cursor = db.cursor()
id = input('enter id')
name = input('enter name')
subject = input('enter sub')
sql = 'insert into faculty(id, name, subject) values(%s, %s, %s)'
val = (id, name, subject)
try:
    cursor.execute(sql, val)
    db.commit()
    print('query executed')
except Exception as e:
    print(e.args)
finally:
    db.close()