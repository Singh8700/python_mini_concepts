
#list create by user
l1=[]
#reandom number create 
x=1
while x<=5:
	#user defined data Enter here
	f1=input(f'''\t\t Enter your fruit name  no {x} : ''')
	#add data in list
	l1.append(f1)
	#incremett by number
	x=x+1
#print list defined by user
l1.sort()
print("\t\t your fruit list is : ",l1)
