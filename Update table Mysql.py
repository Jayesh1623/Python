import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jayesh@079",
    database="myfirstdb"
    )

mycursor = mydb.cursor()

# sql = " update customers set name = 'Rahul' where name = 'Jayesh'"

# mycursor.execute(sql)

sql = " update customers set name = %s where name = %s"
val = ("Jayesh", "Rahul")

mycursor.execute(sql, val)

mydb.commit()