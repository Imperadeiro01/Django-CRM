import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'Anklespooks123'

	)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE company")

print("All done!")

