from gameContinue import  *

while(True):
	# single line inheritance class
	class myclass:
		def myfunction(self):
			print("          It's a parent class :) ")
			x=5
	
	class mysecclass(myclass):
		def myfunction2(self):
			print("         it's a child class :) ")
			
	
	main=mysecclass()
	print(main.myfunction())
	gameContinue()
	#Multilevel inheritance class
	#parent class -> sub_parent class ==> child class
	class parent: #parent class 
		def function1(self):
			print(".           This is a1 class called ")
		
	class Sub_Parent(parent): #sub_parent class
		def function2(self):
			print(".           This is a2 class called ")
			
	class child(Sub_Parent): #chlid class
		def function3(self):
			print("          This is a3 class called")
			
	#create a object for child class only		
	
	maltilavel_class=child()
	print(maltilavel_class.function1())
	print(maltilavel_class.function2())
	print(maltilavel_class.function3())
	gameContinue()
	#Maltiple inheritance class 
	#parent class , 2nd_parent class , 3rd parent class ==> child class
	class Multilevel_parent:#parent class
		def function4(self):
			print(".          this is multiple inheritance class no A1 ")
	class Multilevel_parent2:#2nd parent class
		def function5(self):
			print(".          this is multiple inheritance class no A2 ")		
			
	class multilavel_Child(Multilevel_parent,Multilevel_parent2):#child class
		def function6(self):
			print(".          this is multiple inheritance class no A3 ")
	
	#create a object for child class only		
	
	maltilavel_class=multilavel_Child()
	print(maltilavel_class.function4())
	print(maltilavel_class.function5())
	print(maltilavel_class.function6())
	gameContinue()
	# Hierarchical inheritance class
	#parent class ==> child class & 2nd class both are used
	#Note (more than one child class but create only one parent class)
	class Hi_single_parent:#single parent class
		def function7(self):
			print("            this is a parent class for hierarchical inheritance class a1")
	
	class Hi_FirstChild(Hi_single_parent):#First Child class & used parent class
		def function8(self):
			print("            this is a child class for hierarchical inheritance class a1")
		
	class Hi_SecChild(Hi_single_parent):#second child class used parent class
		def function9(self):
			print("            this is a child class for hierarchical inheritance class a2")
	
	#Create 2 objects because create a 2 child in this section
	#Note (more than one child class but create only one parent class)so you create more than object
	
	Hierarchical_Object1=Hi_FirstChild()
	Hierarchical_Object2=Hi_SecChild()
	
	#Firat child class object
	print(Hierarchical_Object1.function7())
	print(Hierarchical_Object1.function8())
	
	#Second child class object
	print(Hierarchical_Object2.function7())
	print(Hierarchical_Object2.function9())
			
			
	gameContinue()
	# Hybrid inheritance class
	#create one parent class 
	class Hybrid_parent:
		def function10(self):
			print("       This is Hybrid inheritance parent class ")
			
	#create First child class & assign parent class
	class Hybrid_child1(Hybrid_parent):
		def function11(self):
			print("          This section is Hybrid inheritance First Child class" )
		
	#create Second child class & assign parent class
	class Hybrid_child2(Hybrid_parent):
		def function12(self):
			print("          This section is Hybrid inheritance Second Child class ")
			
	#last create 3rd class & assign First_child & Second_child are both 
	class Hybrid_lastChild(Hybrid_child1,Hybrid_child2):
		def function13(self):
			print("          This section is Last Hybrid inheritance Child class ")
			
	#create 3rd child class object only 
	#& get all classes calues
	Hybrid_Obj=Hybrid_lastChild()
	#parent class colled
	print(Hybrid_Obj.function10())
	#First class colled
	print(Hybrid_Obj.function11())
	#Second class colled
	print(Hybrid_Obj.function12())
	#last Class colled
	print(Hybrid_Obj.function13())
	