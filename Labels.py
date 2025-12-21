from tkinter import *

top=Tk() #created the output screen
top.title("Login Me") #add the title of the screen at the top
top.geometry("450x300")#sets the width and height of the output screen
top.config(background = "blue")
#the label for username
user_name=Label(top,text="User Name").place(x=40,y=60)
user_password=Label(top,text="Password").place(x=40,y=100)
#submit button
submit_button=Button(top,text="Submit").place(x=40,y=130)
#Entry Boxes
user_name_input = Entry(top,width=30).place(x=110,y=60)
user_password_input = Entry(top,width=30,show='*').place(x=110,y=100)

#start the screen
top.mainloop()