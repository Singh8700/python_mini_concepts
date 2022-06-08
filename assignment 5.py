#Q1 create file & read
value=str(input(".    Enter your file content : "))
file=open("a.txt","w")
print()
file.write(value)
print(".       File is successful create")
print()
file=open("a.txt","r")
filecontent=file.read()
print(".       your file content is : ",filecontent)
file.close()

#Q2 read file
print()
file=open("a.txt","r")
fileContent=file.read()
print(".     file content is :   ",fileContent)
file.close()

#Q3 append text in exiting file
print()
value=str(input(".    Enter your file update data : "))
file=open("a.txt","a")
file.write(value)
print(".      file successfully update")
print()
file=open("a.txt","r")
fileupdate=file.read()
print(".       file updated data is : ",fileupdate)
file.close()

#Q4 list given value store the file
l1=["Mango","Orange","Apple" ]
file=open("list.txt","w")
file.writelines(l1)
print(".      file successfully update")
print()

#Q 5 read list exiting file

file=open("list.txt","r")
fileupdate=file.readline()
print(".       file updated data is : ",fileupdate)
file.close()

