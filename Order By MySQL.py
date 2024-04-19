# import mysql.connector

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password='Jayesh@079',
#     database="myfirstdb"
# )

# mycursor = mydb.cursor()

# sql = 'select * from customers order by name'

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#     print(x)
    
    
    
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password='Jayesh@079',
    database="myfirstdb"
)

mycursor = mydb.cursor()

sql = 'select * from customers order by name Desc'

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)