import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jayesh@079",
    database="myfirstdb"
)

mycursor = mydb.cursor()

# sql = "Delete from customers where pin = 424101"

sql = "Delete from customers where pin = %s"
pin = (424101,)

mycursor.execute(sql, pin)

mydb.commit()

print("No of record deleted:", mycursor.rowcount)

