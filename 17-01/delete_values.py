import mysql.connector as c
mydb = c.connect(
    host="localhost",
    user="root",
    password="system",
    database="mydatabase"
)
mycursor = mydb.cursor()
mycursor.execute(DELETE from classes where strength=65;)
print("yes")
mydb.commit()
