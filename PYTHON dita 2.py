import mysql.connector

ID = (input("Vendosni ID"))
Emer = (input("Vendosni Emer"))
Mbiemer = (input("Vendosni Mbiemer"))
Email = (input("Vendosni Email"))
Password = (input("Vendosni Password"))

myconn = mysql.connector.connect(host="localhost", user="root", password="", database="letiona")
cur = myconn.cursor()
sql = "insert into user(Id_Card, Emer,Mbiemer, Email, Password) values (%s, %s, %s, %s, %s)"
val = (ID, Emer, Mbiemer, Email, Password)
try:
   # inserting the values into the table
   cur.execute(sql, val)
   myconn.commit()
except:
     myconn.rollback()
print(cur.rowcount, "record inserted!")
myconn.close()