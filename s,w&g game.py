
from gameContinue import *
from random import *



#create a game sneak, water & gun
def gamewin(comp,user):
	if(comp == user):
		print("       Game tried now")
		#computer choice s
	elif(comp == 's'):
		if(user=='w'):
			return  False
		elif(user=='g'):
			return  True
#comouter choice w
	elif(comp == 'w'):
		if(user=='g'):
			return  False
		elif(user=='s'):
			return  True
#computer choice g
	elif(comp == 'g'):
		if(user=='s'):
			return  False
		elif(user=='w'):
			return  True
while True:			
	turn = randint(1,3)
	#print(turn)
	if(turn == 1):
			comp = "s"
	elif(turn==2):
			comp="w"
	elif(turn==3):
			comp="g"
	#Game function



	
		
	
	
	

	print(".      Game roles: Sneak(s) , Water(w) & Gun(g) select only")
	print()
	
	print("      computer's true : ")
	user=input("       Your's turn : ")
	
	a=gamewin(comp,user)
	print()
	if a==None:
		print(".       Game is tie ! ")
	elif a:
		print(".      You Win")
	else:
		print(".      You loss")
		
	print()
	print(".      computer select is :",comp)
	print()
	gameContinue()