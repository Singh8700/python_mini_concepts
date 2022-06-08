from gameContinue import *

#gameContinue()

class myclass:
	def __init__(self):
		while(True):
			try:
				user1=int(input("          Please Enter the first values : "))
				user2=int(input("         Please Enter the Second values : "))
				print("          your value sum is : ",user1+user2)
				gameContinue()
			except Exception as e:
				print("         you enter the wrong value please check : ",e)
				gameContinue()
			
			
			
			


obj1=myclass()
print(obj1)
