# import mysql.connector

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Jayesh@079",
#     database="myfirstdb"
# )

# mycursor = mydb.cursor()

# sql = "INSERT INTO customers (name, city, pin) VALUES (%s, %s, %s)" 
# val = ("Jayesh", "NK", 423404)

# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "Record Inserted")



import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jayesh@079",
    database="myfirstdb"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, city, pin) VALUES (%s, %s, %s)" 
val = [
       ("Aadi", "Patna", 423404),
       ("Yash", "Pune", 456733),
       ("Veera", "Mumbai", 412022),
       ("Abhi", "Nagpur", 489432)
       ]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "Record Inserted")