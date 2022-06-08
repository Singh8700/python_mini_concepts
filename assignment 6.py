#use exception in py
#Q1
try:
	user1,user2=int(input(".       Enter the first values :")),int(input(".     Enter the Second values :"))
	print(".            ",type (user1) == type(user2))
	print(".         ",type(user1))
	print(".         ",type(user2))
except Exception as e:
		print(".     something went wrong ",e)
		
#Q2
try:
	print()
	user1,user2=str(input(".       Enter the first values :")),str(input(".     Enter the Second values :"))
	print(".            ",type (user1) == type(user2))
	print(".         ",type(user1))
	print(".         ",type(user2))
except Exception as e:
		print(".     something went wrong ",e)
		
		
#Q3
try:
	print()
	user1,user2=int(input(".       Enter the first values :")),int(input(".     Enter the Second values :"))
	print(".            ",type (user1) == type(user2))
	print(".         ",type(user1))
	print(".         ",type(user2))
	print(".         Your sum is : ",user1+user2)
except Exception as e:
		print(".     something went wrong ",e)
finally:
		print("          bye")
		
#Q4
try:
	user1,user2=int(input(".       Enter the first values :")),int(input(".     Enter the Second values :"))
	print(".            ",type (user1) == type(user2))
	print(".         ",type(user1))
	print(".         ",type(user2))
except Exception as e:
		print(".     something went wrong ",e)
else:
	print("      Pleas check the values ")
finally:
	print("          bye")