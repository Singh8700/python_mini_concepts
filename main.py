#Assesment 3
#game loop is start
def gameCon():
	userPremission=str(input(".   Do you want continue (Yes/No) : "))
	if(userPremission==" YES" or userPremission=="yes" or userPremission=="Y" or userPremission=="y"):
		return 
	else:
		exit()
#Q1 solved user defined list & Q 4 solved
L1=[]
user1=input(".    create a list : ")
L1.insert(1,user1)
print(".    you create this list")
print("     Your list is :     ",L1)
print()
uservalue=str(input(".      Do you want continue (Yes/No) : "))
userPermission=uservalue.casefold()
	
#Q2 solved remove 3 in this list

l2=[1,2,3,4,5,6,7,8,9]
print("         current list is : ",l2)
l2.remove(3)
print(".         updated list is : ",l2)
print()
	
	#Q3 solved add Python in index no 2 in list
gameCon()
l3=[" Java"," Php"," Net"," Angular"]
print(".      Current list is : ",l3)
l3.insert(2," Python")
print(".      updated list is : ",l3)
print()
	#Q4 solved create list into loop
gameCon()
l5=[]
x=0
	
while x<=5:
	user=input(".       create the multiple value list : ")
	l5.insert(1,user)
	x=x+1
	
print("     your list is : ",l5)
print()
	#Q5 solved create a tuple
gameCon()
t1=("Paython",1,2,3,"Java",'A','B')
print("        Current tuple is : ",t1)
print()
for i in t1:
	print(".       your tuple is :",i)
			
	print()
	print("         index value 5 is : ",t1[5])
		#Q6 solved count tuple 
	gameCon()
	print(".        length of tuple is : ",len(t1))
	print(".        0 to 5 index values is :",t1[:5])
	print("          last index value is : ",t1[-1])
print()
		#Q7 solved tuple convert into list
gameCon()
l4=list(t1)
print(".       current tuple is : ",t1)
print(".        convert tuple into list : ",l4)
print()
		#Q8 list create into dictionary
gameCon()
d1={"list":[1,2,3,4,5], "list2":("A","B","C","D","E")}
print("        your dictionary is : ",d1)
print()
print(".       This  is : ",type(d1))
print()
print(".       First dictionary is : ",d1["list"])
print()
print(".       This is : ",type(d1["list"]))
print()
print(".       Second dictionary is : ",d1["list2"])
print()
print(".       This is : ",type(d1["list2"]))
print()
		
		#Q9 solved print key & convert key into list
gameCon()
d2={1:"Pytho",2:"Java",3:"JavaScript",4:"HTML",5:"CSS" }
print(".     current  key is : ",d2.keys())
print("     current  values is : ",d2.values())
print(".    current type is : ",type(d2))
		#after updated
		#Q10 solved print values on keys & convert values into list
gameCon()
list3=list(d2.keys())
list4=list(d2.values())
print("      after updated : ",list3)
print(".     after updated values convert list : ",list4)
		
gameCon()