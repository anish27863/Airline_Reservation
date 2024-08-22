import pandas as pd
import mysql.connector
con=mysql.connector.connect(host='127.0.0.1',user='Anish',passwd='12345',database='airline')
cursor=con.cursor()

def planes_available():
 cursor.execute('SELECT * FROM planes')
 result=cursor.fetchall()
 for i in result:
    print(i)

planes_available()