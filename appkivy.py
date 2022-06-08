#import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class MyApp(GridLayout):
	
	def __init__(self,**kwargs):
		super(MyApp, self).__init__()
		#create a column in our app
		self.cols=1
		#set the label of your entered data
		self.add_widget(Label(text="Enter Name"))
		#add text box in our app
		self.s_name = TextInput()
		self.add_widget(self.s_name)
		#new widget add in our app
		#set the label of your entered data
		self.add_widget(Label(text="Enter Last Name :"))
		self.l_name = TextInput()
		self.add_widget(self.l_name)
	
class SpartanApp(App):
	
	def build(self):
		return MyApp()

SpartanApp().run()