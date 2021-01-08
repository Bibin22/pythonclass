import mysql.connector
def get_connect():
    db = mysql.connector.connect(host='localhost', user='bibin', passwd='1234', database='cms')
    return db