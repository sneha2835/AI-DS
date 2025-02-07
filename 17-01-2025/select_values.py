import mysql.connector as c

mydb = c.connect(
    host="localhost",
    user="root",
    password="system",
    database="mydatabase"
)
mycursor=mydb.cursor()
mycursor.execute("select * from classes ")
students=mycursor.fetchall()
for std in students:
    print(std)
mydb.commit()
