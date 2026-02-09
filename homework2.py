from tkinter import *
from tkinter.filedialog import *

root = Tk()
root.title("Address Book")
root.geometry("600x400")


def open():
    fin = askopenfile(title="Open File")
    if fin is not None:
        box.delete(0, END)
        for line in fin.readlines():
            box.insert(END, line.strip())

def delete():
    select=box.curselection()
    if select:
        index=select[0]
        box.delete(index)

def add():
    fetch=name.get()+" "+address.get()+" "+mobile.get()+" "+email.get()+" "+bday.get()
    box.insert(END,fetch)
    name.delete(0,END)
    address.delete(0,END)
    mobile.delete(0,END)
    email.delete(0,END)
    bday.delete(0,END)

def save():
    out=asksaveasfile(defaultextension=".txt")
    if out is not None:
        for item in box.get(0,END):
            print(item,file=out)


     


Label(root, text="Address Book", font=("Arial", 14)).place(x=230, y=10)
Label(root, text="Name").place(x=300, y=60)
Label(root, text="Address").place(x=300, y=90)
Label(root, text="Mobile").place(x=300, y=120)
Label(root, text="Email").place(x=300, y=150)
Label(root, text="Birthday").place(x=300, y=180)


name = Entry(root, width=25)
name.place(x=370, y=60)

address = Entry(root, width=25)
address.place(x=370, y=90)

mobile = Entry(root, width=25)
mobile.place(x=370, y=120)

email = Entry(root, width=25)
email.place(x=370, y=150)

bday = Entry(root, width=25)
bday.place(x=370, y=180)


Button(root, text="OPEN", width=10, command=open).place(x=100, y=50)
Button(root, text="DELETE", width=10, command=delete).place(x=200, y=50)
Button(root, text="SAVE", width=10).place(x=100, y=300)
Button(root, text="UPDATE / ADD", width=15 , command=add).place(x=370, y=220)
Button(root, text="SAVE",width=10,command=save).place(x=380,y=260)


box = Listbox(root, width=30, height=15)
box.place(x=50, y=100)

root.mainloop()