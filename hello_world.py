import mysql.connector
print('hello world1')
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="secure"
)
print(mydb)
