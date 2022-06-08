import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


class MyApp(App):
	
	def build(self):
		return Label(text="Hello wolrd H787")
	

if __name__ == "__main__":
	MyApp().run()