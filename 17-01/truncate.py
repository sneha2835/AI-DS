import mysql.connector as c

mydb = c.connect(
    host="localhost",
    user="root",
    password="system",
    database="mydatabase"
)

mycursor = mydb.cursor()

sql = "TRUNCATE TABLE classes"

mycursor.execute(sql)

print("yes")

mydb.commit()
