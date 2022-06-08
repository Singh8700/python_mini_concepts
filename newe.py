set1={1,7,2,9,2,9,}
s="\t"
print(s,set1)
#create empty set
set2 = set()
print(s,type(set2))
x=1
while x<=10:
	try:
		user=int(input("\tEnter your set data :"))
		set2.add(user)
		x=x+1
	except Exception as e:
		print(" \tworng values entered \n\t",e)
print (s,"Set not except repeated values ",set2)

#remove the set value
allow=input("\t Allow to remove set values (y/n) : ")
if allow == 'y':
	try:
		print(s,"See your set",set2)
		user=int(input("\t Enter remove values: "))
		set2.remove(user)
		print("\t after removing your set",set2)
	except Exception as e:
		print("\tEnter right values ",e)
