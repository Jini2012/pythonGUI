from tkinter import *
from tkinter.filedialog import *
root= Tk()
root.geometry("400x400")
def add():
    guess=task.get()
    box.insert(END,guess)
def save():
    out=asksaveasfile(defaultextension=".txt")
    if out is not None:
        for item in box.get(0,END):
            print(item,file=out)
    else:
        print("ERROR ERROR I REPEAT ERRORRRR")
def delete():
    select=box.curselection()
    if select:
        index=select[0]
        box.delete(index)
def open():
    fin=askopenfile(title="Open File")
    if fin is not None:
        box.delete(0,END)
        list=fin.readlines()
        for i in list:
            box.insert(END,i)

L1 = Label(root , text="Memorizer")
L1.place(x=160,y=30)
B1 = Button(root,text="  OPEN  ",command=open)
B1.place(x=100,y=60)
B2 = Button(root,text="  DELETE  ",command=delete)
B2.place(x=200,y=60)
B3 = Button(root,text="  SAVE  ",command=save)
B3.place(x=300,y=60)
B4 = Button(root,text="  ADD  ",command=add)
B4.place(x=300,y=100)
task=Entry(root,width=30)
task.place(x=100,y=100)
box=Listbox(root,width=30)
box.place(x=100,y=150)
root.mainloop()