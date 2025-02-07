import mysql.connector as c

mydb = c.connect(
    host="localhost",
    user="root",
    password="system",
    database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO classes VALUES ('ds', 'b', 65), ('cse', 'b', 64);"

mycursor.execute(sql)

mydb.commit()
