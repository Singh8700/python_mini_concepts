#user definet number
while(True):
	userContinue = str(input("          Do you want Play this Game (Yes/No)  : "))
	if(userContinue == "Yes" or userContinue== "yes" or userContinue=="y"):
		#Q1 solved 
	#	space= 0
#		space.center(40) 
		userNam = int(input("         Provide the number  & check is Odd/Even : "))
		if(userNam%2 == 0):
			print("          ","Your number is Even : ",userNam)
		else:
			print("           ","Your number is Odd : ",userNam)
		print()
		#Q2 solved
		userNum = int(input("          Enter the First Number (Check greater number ) : "))
		userNum1 =  int(input("        Enter the Second Number (Check greater number ) : "))
		if(userNum == userNum1):
			print("        ","Values are same not greter & less")
		elif(userNum > userNum1):
			print("         ","Your Fisrt numer is greter than  Second number : ",userNum)
		else:
			print("          ","Your Second numer is greter than  First number : ",userNum1)
			print()
		#Q5 Solved
		print()
		Snum=int(input("        Enter Starting Number : "))
		Enum = int(input("        Enter Ending Number : "))
		for i in range(Snum,Enum):
			for j in range(i):
				print("    ",j,end=" ")
			print("    ",i)
		print()
		#while loop end 
	else:
		break
		


