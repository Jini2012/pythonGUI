from tkinter import *
from tkinter.ttk import *
from time import strftime #it allows to get the current time.
#creating tkinter window.
root=Tk()
root.title("Menu Demonstration")
#Creating Menubar  
menubar=Menu(root)

#Adding File Menu
file = Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=file)
file.add_command(label='New File',command=None)
file.add_command(label='Open',command=None)
file.add_command(label='Save',command=None)
file.add_separator()
file.add_command(label='Exit',command=root.destroy)

#Add Edit Menu
edit = Menu(menubar,tearoff=0)
edit.add_command(label='Edit',command=None)
edit.add_command(label='Cut',command=None)
edit.add_command(label='Copy',command=None)
edit.add_command(label='Paste',command=None)
edit.add_command(label='Select all',command=None)
edit.add_separator()
edit.add_command(label='find',command=None)
edit.add_command(label='File again',command=None)
#Add Help Menu 
help=Menu(menubar,tearoff=0)
help.add_cascade(label='Help',command=None)
help.add_command(label='Demo',command=None)
#display Menu
root.config(menu=menubar)
root.mainloop()