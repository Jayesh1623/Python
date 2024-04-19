# import mysql.connector

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Jayesh@079",
#     database="myfirstdb"
# )

# mycursor = mydb.cursor()

# mycursor.execute("Select * from customers Where City = 'pune'")

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

sql= "select * from customers where name like 'A%' order by name "

mycursor.execute(sql)

myresult= mycursor.fetchall()

for x in myresult:
    print(x)



# import mysql.connector

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Jayesh@079",
#     database="myfirstdb"    
# )

# mycursor = mydb.cursor()

# sql= "select * from customers where pin = %s"  # To avoid sql injection escape query values by using placeholder %s
# pin = (424101,)

# mycursor.execute(sql, pin)

# myresult = mycursor.fetchall()

# for x in myresult:
#     print(x)


