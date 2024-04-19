# import mysql.connector

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Jayesh@079",
#     database="myfirstdb"
# )

# mycursor = mydb.cursor()

# sql = "drop table employee"

# mycursor.execute(sql)



import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jayesh@079",
    database="myfirstdb"
)

mycursor = mydb.cursor()

sql = "drop table if exists employee"

mycursor.execute(sql)