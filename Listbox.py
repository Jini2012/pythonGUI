import tkinter as tk

root= tk.Tk()
root.geometry("300x150")
scroll=tk.Scrollbar(root)
scroll.pack(side="right", fill="y")

list=tk.Label(root,text="I wanna be yours : Lyrics").pack(side="top")
listbox=tk.Listbox(height=15,width=100 , bg= "black", fg="silver",yscrollcommand=scroll.set)
listbox.insert(1,"I wanna be your vacuum cleaner")
listbox.insert(2,"Breathing in your dust")
listbox.insert(3,"I wanna be your Ford Cortina")
listbox.insert(4,"I will never rust")
listbox.insert(5,"If you like your coffee hot")
listbox.insert(6,"Let me be your coffee pot")
listbox.insert(7,"You call the shots, babe")
listbox.insert(8,"I just wanna be yours")
listbox.insert(9,"Secrets I have held in my heart")
listbox.insert(10,"Are harder to hide than I thought")
listbox.insert(11,"Maybe I just wanna be yours")
listbox.insert(12," wanna be yours, I wanna be yours")
listbox.insert(13,"Wanna be yours")
listbox.insert(14,"Wanna be yours")
listbox.insert(15,"Wanna be yours")
scroll.config(command=listbox.yview)


listbox.pack()
root.mainloop()