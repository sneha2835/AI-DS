import mysql.connector as c

mydb = c.connect(
    host="localhost",
    user="root",
    password="system",
    database="mydatabase"
)

mycursor = mydb.cursor()

sql = "UPDATE classes SET branch = 'aiml' WHERE strength = 64;"

mycursor.execute(sql)

print("yes")

mydb.commit()
