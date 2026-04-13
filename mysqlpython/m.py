import mysql.connector
con=mysql.connector.connect(
	host="localhost",
	user="root",
	password="ROOT",
	database="aryan"
)
if con:
	print("connected")
else:
	print("not connected")