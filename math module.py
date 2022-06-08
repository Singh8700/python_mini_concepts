from gameContinue import *
from math import *
from random import *

class myclass:
	def __new__(self):
		while(True):
			try:
				x=randint(100,999)
				print("       Your Otp is :   ",x)
				user1=int(input("        Enter your Otp : "))
				if(user1==x):
					print("       Otp is Correct")
					gameContinue()
				else:
					print("       Otp is Incorrect")
					gameContinue()
			except Exception as e:
				print("        worng values : ",e)
				gameContinue()
		
		
		
		
obj1=myclass()
print(         obj1)
