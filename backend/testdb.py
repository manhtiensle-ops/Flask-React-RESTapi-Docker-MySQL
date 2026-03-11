import mysql.connector
from mysql.connector import Error
import time


cnx=mysql.connector.connect(host='db',
                            user='root',
                            password='password',
                            database='LOGIN',
)
cursor=cnx.cursor()
cursor.execute("SELECT * FROM LOGIN;")
tables=cursor.fetchall()
cursor.close()

print(tables)

cnx.close()

