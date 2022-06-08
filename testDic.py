# dictionary 

myDic={
	"name":"Rohit",
	"age":22,
	"Education":"graduate"
}
#myDic.clear()
s="\t"
n=" \n"
print(s,myDic.keys())
print(n,s,myDic.values())
print(n,s,myDic.items())

#update dictionary
UpDic={
	"Kumar":"Friends",
	"Singh":"Last Name",
}
myDic.update(UpDic)

print(n,s,myDic.get("minor"))
