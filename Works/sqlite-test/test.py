import sqlite3
from typing import Text

conn=sqlite3.connect('ders.db')
print('salam')

cursor= conn.cursor()
print("cursor hazirdi")

# cursor.execute ("""DROP TABLE IF EXISTS STUDENTS""")

# cursor.execute(""" CREATE TABLE STUDENTS (
#     name Text,
#     lastname text,
#     age integer
# )""")
# print("Tablo hazir")
add_command= """INSERT INTO STUDENTS VALUES {}"""
data1=('Rehman','Esrefov', 26)
cursor.execute(add_command.format(data1))

conn.commit()
conn.close()