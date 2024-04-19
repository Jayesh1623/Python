"""To work with MySQL database python needs MySQL driver so we will use 
MySQL connector driver to work with database, so we will required to download & Install MySQL connector first,
for that go to command line interface & download the driver using 'PIP Install MySQL-connector-python'  """


import mysql.connector

mydb = mysql.connector.connect(
    host= "localhost",
    user= "root",
    password="Jayesh@079"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE myfirstdb")

mycursor.execute("Show Databases")

for x in mycursor:
    print(x)
