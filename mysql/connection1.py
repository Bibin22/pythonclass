import mysql.connector
db = mysql.connector.connect(host='localhost', user='bibin', passwd='1234', database='cms')
cursor = db.cursor()
sql = 'SELECT VERSION()'
cursor.execute(sql)
data = cursor.fetchone()
print(data)