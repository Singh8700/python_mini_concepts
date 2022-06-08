from tkinter import *
import tkinter.messagebox as m
r=Tk()
r.geometry("30x30")
r.title("My phone")
r.configure(bg="green")
ln=Label(r,text="Roll No enter now")
ln.place(x=20,y=20)
en= Entry()
en.place(x=500,y=20)
def sho():
	return  m.showinfo("hello","hi bro")
sb=Button(r,text="Submit",bg="red", command=sho())
sb.place(x=20,y=100)

mainloop()



