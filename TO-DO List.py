from tkinter import *
top = Tk()
top.geometry("500x400")
def add():
    guess=task.get()
    box.insert(END,guess)
def delete():
    select=box.curselection()
    if select:
        index=select[0]
        box.delete(index)
def del_all():
    box.delete(0,END)
def del_task():
    task.delete(0,END)
heading=Label(top,text="TO-DO LIST").place(x=160,y=30)
heading2=Label(top,text="ENTER THE TASK").place(x=10,y=60)
task= Entry(top,width=30)
task.place(x=110,y=60)
addbt=Button(top,text="Submit",command=add).place(x=165,y=90)
box=Listbox(top,width=30)
box.place(x=100,y=120)
deletebt=Button(top,text="Delete",command=delete)
deletebt.place(x=165,y=300)
clear_button=Button(top,text="Clear",command=del_task)
clear_button.place(x=250,y=90)
delall=Button(top,text="Delete All",command=del_all)
delall.place(x=250, y=300)
top.mainloop()
