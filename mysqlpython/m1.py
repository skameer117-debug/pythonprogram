import mysql.connector
con=mysql.connector.connect(
	host="localhost",
	user="root",
	password="ROOT",
	database="aryan"
)
print("connected sucessfully")
cur=con.cursor()
cur.execute("select * from student")
rows=cur.fetchall()
print("\nStudent Records:\n")
for r in rows:
	print("roll no:",r[0])
	print("Name   :",r[1])
	print("Marks  :",r[2])
	print("-------------------------------")
con.close()
