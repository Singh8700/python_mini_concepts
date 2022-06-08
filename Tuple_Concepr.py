#tuple all concepts are clear
#fist create blank tuple
t1=()

#second inster data in tuple from user
print("\n\t Before inster tuple : ",t1)
x=1
while x <=5:
	userInster=input(f"\t Enter your tuple data {x} :")
	#firat convert tuple into list
	l1=list(t1)
	#than insert data
	l1.append(userInster)
	#than again convert list into tuple
	t1=tuple(l1)
	x=x+1
print("\n\tAfter inster data your tuple :",t1)

#count of content in tuple
print (" \n\t Total tupe is : ",len(t1))
userIndex=str(input("\n\tCheck tuple index :"))
print("\n\tTuple index is :",t1.index(userIndex))

#Replace tuple content
#first tuple convert into list

print("\n\t Current tuple after List",l1)
try:
	x=int(input("\n\t Enter the index no :"))
	userReplace=input("\n\tEnter replace Content :")
	l1[x]= userReplace
	print("\n\t After replace list Content :",l1)
	#second again convert list into tuple
	t1=tuple(l1)
	print("\n\t After convert list into tuple content : ",t1)
	
except Exception as e:
	print(" \n\t please enter the right value :\n\t",e)

	







