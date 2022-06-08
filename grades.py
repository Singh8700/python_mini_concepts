		#Q3 solved
		#hindi here
while(True):
	print()
	print()
	user=input("         Do you want calculate your marks (Yes/No) : ")				
	if(user=="yes" or user=="Yes" or user=="y"):
		hindi = int(input("          Enter your Hindi Marks : "))
		if(hindi>=101):
			print("           Please enter right value")
			print()
		elif(hindi<33):
			print("           compartment this Subject")
			print()
		else:
			#English here
			english = int(input("          Enter your English Marks : "))
			if(english>=101):
				print("          Please enter right value")
			elif(english<33):
				print("          compartment this Subject")
			else:
				#Math here
				math = int(input("          Enter your Math Marks : "))
				if(math>=101):
					print("          Please enter right value")
				elif(math<33):
					print("          compartment this Subject")
				else:
					#Science here
					science = int(input("          Enter your Science Marks : "))
					if(science>=101):
						print("          Please enter right value")
					elif(science<33):
						print("          compartment this Subject")
					else:
						#Sacol-Science here
						sacol_science= int(input("          Enter your Sacol-Science Marks : "))
						if(sacol_science>=101):
							print("          Please enter right value")
						elif(sacol_science<33):
							print("          compartment this Subject")
						else:
							#) now calculation time is here
							print()
							#total marks calculation
							total=hindi+math+science+english+sacol_science
							#total marks calculation percentage
							per=total/5
							print("          Your Total Marks is : ",total)
							print()
							print("          Your Total percentage is : ",per," %")
							print()
						#providing the percentage according to grade
							if(per>=80):
								print("          congratulations You have A+ grade. Excellent Work")
							elif(per>=70):
								print("          congratulations You have A grade. Very Good Work")
							elif(per>=65):
								print("          congratulations You have B+ grade. Good Work")
							elif(per>=60):
								print("          congratulations You have B grade. Nice Work")
							elif(per>=55):
								print("          congratulations You have C+ grade. Good Work")
							elif(per>=45):
								print("          congratulations You have C grade. Not Bad Work")
							elif(per>=33):
								print("          congratulations You have D grade. improve your marksheet ")
							else:
								print("Your are Fail please retry your Exam")

	else:
		break
	
	
	
					
		
			
		
		
		
		
		