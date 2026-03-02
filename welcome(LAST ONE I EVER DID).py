from tkinter import *
root=Tk()
root.geometry("300x300")
def message():
  name= E.get()
  L1.config(text="WELCOME "+name +"!!")
  E.delete(0,END)
B1=Button(root,text="PLACE",command=message)
B1.place(x=130,y=120)
E=Entry(root,width=30)
E.place(x=75,y=95)
L1=Label(root,text="")
L1.place(x=110,y=150)

root.mainloop()