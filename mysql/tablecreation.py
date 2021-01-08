#import mysql.connector
from dbconnection.dbconnect import *
db = get_connect()
cursor = db.cursor()
sql = 'create table faculty(id varchar(20), name varchar(50), subject varchar(50))'
try:
    cursor.execute(sql)
    print('table succesfully created')
except Exception as e:
    print(e.args)
finally:
    db.close()