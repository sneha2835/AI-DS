import mysql.connector as c
mydb = c.connect(
    host="localhost",
    user="root",
    password="system",
    database="mydatabase"
)
mycursor = mydb.cursor()
mycursor.execute(select *from classes order by desc;)
mycursor.execute(select *from classes where branch='ds';)
print("yes")
mydb.commit()
