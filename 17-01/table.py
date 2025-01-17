import mysql.connector as c

mydb = c.connect(
    host="localhost",
    user="root",
    password="system",
    database="mydatabase"
)

mycursor = mydb.cursor()

sql = "create table classes (branch varchar(20) primary key, section varchar(20), strength int);"

mycursor.execute(sql)

mydb.commit()
