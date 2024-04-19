import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jayesh@079",
    database="myfirstdb"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE customers (name VARCHAR(250), city VARCHAR(250), pin VARCHAR(250))")

mycursor.execute("Show Tables")

for x in mycursor:
    print(x)


# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")