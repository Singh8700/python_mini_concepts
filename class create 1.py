#pylint:disable=E0001
#create the class in python program
class myclass:
	x="     Rohit"
	def myfun(self):
		print(".       function is successfully created")
	def secFun(self):
		print(".     second function")
print(myclass.x)
print(myclass().myfun(),myclass().secFun())

#constractor create here
class myclass2:
	def __init__(self):
		print("         successfully2 created")
		
cl2=myclass2()
print (cl2)

#class values update & Delete
class myclass3:
	def __init__(self,name,age,clas):
		self.name = name
		self.age= age
		self.clas= clas
	def myfun3(self):
		print(             self.name)

user = myclass3("Rohit",22,"Graduate")

print(user.name)
print(user.age)
user.age = 21
del user.name
print(user.age)
