#pylint:disable=E0001
#write the file
def writ(fileName,fileContent):
	file=open(fileName,"w")
	file.write(fileContent)
	print("file is created ")
	file.close()
	
#file read now
def red(fileRead):
	file=open(fileRead,"r")
	filecontent= file.read()
	print(".            " ,filecontent)
	file. close()
	
def runread():
 	userPremission=str(input(".   Do you want Read file  (Yes/No) : "))
 	if(userPremission==" YES" or userPremission=="yes" or userPremission=="Y" or userPremission=="y"):
 		fileRead=str(input(".      Enter the file name which file you read : "))
 		red(fileRead)
 	else:
 		#exit()
 		print("       Oky")
 		
 #apped & update the file
def appen(fileName,updateData):
	file=open(fileName,"a")
	print()
	file.write(updateData)
	print("      file is update")
	file.close()

def runupdate():
 	userPremission=str(input(".   Do you want update  file content  (Yes/No) : "))
 	if(userPremission==" YES" or userPremission=="yes" or userPremission=="Y" or userPremission=="y"):
 		fileName=str(input(".      Enter the file name which file you Update : "))
 		updateData=str(input(".      Enter the file update content : "))
 		appen(fileName,updateData)
 	else:
 		exit()
 		

	
fileName=str(input(".      Enter the file name :  "))
fileConten=str(input(".      Enter the file Content :  "))

writ(fileName,fileConten)
runread()
runupdate()
runread()
