#import mysql connector module
import mysql.connector as s

#create a variable to connect mysql
db= s.connect(host="localhost",port=3306,user="u0_a251",password="admin")

#create new database in mysql
def createDatabase(c):
	cor=db.cursor()
	database=(c)
	query = "create database "+database
	cor.execute(query)
	db.commit()
	db. close()

#create("Std")

#Delete database in mysql
def deleteDatabase(d):
	cor=db.cursor()
	dele=(d)
	query= " drop database "+dele
	cor.execute(query)
	print(".     successfully deleted database")
	db.commit()
	db.close()
	
#delete("Std" )

#create Table is database
def createTable(c):
	cor=db.cursor()
	query = c
	cor.execute(query)
	db.commit()
	db. close()

#delete table in database
def deleteTable(d):
	cor=db.cursor()
	dele=(d)
	query="drop table "+dele
	cor.execute(query,dele)
	print(".     successfully deleted database")
	db.commit()
	db.close()

#db1=s.connect(user="u0_a251",password="admin", database=createDatabase)