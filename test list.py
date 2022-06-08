name=input("     Type your name here : ")

#print user name
print(".    Good afternoon ",name)

#Date = input(".    Enter the Date : ")

#email='''       Dear <|name|>
#		you are selected
#	<|Date|>'''
#email=email.replace("<|name|>",name)
#email=email.replace("<|Date|>",Date)
#print(email)


l1=[]
x=1
while x<=5:
	try:
		user=int(input(f"\t Enter you maskes {x}: "))
		l1.append(user)
		x=x+1
		l1.sort()
	except Exception as e:
		print(f"\n\tplease enter right value {name}\n\t",e,"\n")

print(" \n\tyour sort list is : ",l1)
print("\n\tyour total sum is : ",sum(l1))

t1 = (1,2,0,2,0,0,0,20,0,)
t2=t1.count(0)
print("\n\t",t1,"\n\t zero is :",t2,"times")