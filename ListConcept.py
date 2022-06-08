#List all concept completewq
'''ist always create in [ ] 
like example:-
l1 = [1,2,3,4,]
this'''
#first create empty list
l1=[]

#list create function
def createList():
	while True:
				try:
					userNo=int(input("\n\tType List Length :"))
					x=userNo
					l=1
					while l<=x:
						userList=input(f"\tEnter list Content {l} : ")
						l1.append(userList)
						l=l+1
					print("\n\t Your List is : ",l1)
					return sortList()
				except Exception as e:
					print("\n\t Please enter right value\n",e)
#createList()





#Update list
def UpdateList():
	userAllow=input ("\n\tDo you want Update current list (yes/no) : ")
	while True:
		if(userAllow == "y" or userAllow == "Yes" or userAllow == "yes" or userAllow == "Y"):
			print("\n\t your current list : ",l1)
			userAllow=input("\n\tEnter new Content in your current list :")
			l1.append(userAllow)
			print("\n\t After Update List : ",l1)			
			return sortList()
		else:
			return sortList()








#sort Current list
def sortList():
	userAllow=input ("\n\tDo you want Sort current list (yes/no) : ")
	if(userAllow == "y" or userAllow == "Yes" or userAllow == "yes" or userAllow == "Y"):
		print("\n\tSee your Current List :",l1)
		l1.sort()
		print("\n\tYour sort list is : ",l1)
		return replace()
	else:
		return replace()
		






# replace list content
def replace():
	userAllow=input ("\n\tDo you want Replace content in list(yes/no) : ")
	while True:
		if(userAllow == "y" or userAllow == "Yes" or userAllow == "yes" or userAllow == "Y"):
			print("\n\tBefore replace list : ",l1)
			x=int(input("\n\t Enter the index no :"))
			userReplace=input("\n\tEnter replace Content :")
			l1[x]= userReplace
			print("\n\t After replace list Content :",l1)
			return removeCon()
		else:
			return removeCon()
	
#Remove Content in list
def removeCon():
	userAllow=input ("\n\tDo you want Remove Contents list (yes/no) : ")
	while True:
		if(userAllow == "y" or userAllow == "Yes" or userAllow == "yes" or userAllow == "Y"):
			print("\n\tSee your Current List :",l1)
			userEnter=input("\n\t Enter remove Content Name : ")
			l1.remove(userEnter)
			print("\n\tAfter remove content List :",l1)
			return againlist()
		else:
			return againlist()


	
		
			

#allow to create list again
def againlist():
	userAllow=input ("\n\tDo you want Add Content in current list (yes/no) : ")
	while True:
		if(userAllow == "y" or userAllow == "Yes" or userAllow == "yes" or userAllow == "Y"):
			return createList()
		else:
			return gameOver()







#create a loop exit function
def gameOver():
	userAllow=input ("\n\tDo you want continue this list Game (yes/no) : ")
	while True:
		if(userAllow == "y" or userAllow == "Yes" or userAllow == "yes" or userAllow == "Y"):
			return againlist()
		else:
			print("\n\t Bye 👋'")
			exit()






#create loop to start - end -start (Infinity loop)
while True:
	createList()

#	print("\n\t Your List is : ",l1)
#removeCon()

			