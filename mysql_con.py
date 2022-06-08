import mysql.connector as s
import sqlite3

con= s.connect(user="u0_a251", password="admin")
	
def connect():

	db= "create database stde"
	cor=con.cursor()
	cor.execute(db)
	con.commit()
	if con.is_connected() == True:
		print(" successfully completed")
	con.close()

#database 
dab=s.connect(user="u0_a251", password="admin", database="stde")
cont = dab.cursor()
def createTable():
	qurey="create table stuInfo(Sid int primary key auto_increment,name varchar(50),age int)"
	cont.execute(qurey)
	print(".       create successfully")
	dab.commit()
	dab.close()

def insert(n,a):
	dat=(n,a)
	qurey="insert into stuInfo(name, age) values (%s,%s)"
	
	cont.execute(qurey,dat)
	print(".      inser successfully data")
	dab.commit()
	dab.close()

insert(" kumar",22)