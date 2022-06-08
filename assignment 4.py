#import gameContinue function
from gameContinue import *


#Q1 create the function us user name & user subject
userName=str(input(".     Enter your Name : "))
userSubject=str(input(".     Enter your Name : "))
def userData(Name,subject):
	print(".    your name is : ",Name)
	print(".    your Subject is :",subject)
	
userData(userName,userSubject)
print()
uesrValues1=int(input("     Enter first values :"))
userValues2=int(input("     Enter first values :"))
		
	#Q2 sum() function defined
def sum(a,b):
	print("    your sum is : ",a+b)

sum(uesrValues1,userValues2)
gameContinue()
#Q3 calculator
def calcu(a,b):
	print(".    addition is :",a+b)
	print("      substrate is :",a-b)
	print(".      multiply is : ",a*b)
	
calcu(userValues2,uesrValues1)
gameContinue()
print()
#Q4 recursion function
def far(x):
	if x == 1:
		return 1
	else:
		return (x*far(x-1))
num=10
print("      The factorial of",num, " is : ",far(num))
gameContinue()
print()

#Q5 

def Sum(a,b):
	print(a+b)

Sum(2,5)
	