# import mysql.connector

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Jayesh@079",
#     database="myfirstdb"
# )

# mycursor = mydb.cursor()

# mycursor.execute("SELECT * FROM customers")

# myresult = mycursor.fetchall()

# for x in myresult:
#     print(x)



import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jayesh@079",
    database="myfirstdb"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT name, city from customers")

# myresult = mycursor.fetchall()

myresult = mycursor.fetchone()  # fetchone() method will return first row of the result

for x in myresult:
    print(x)