from tkinter import *
import random
import tkinter.messagebox
root= Tk()
root.geometry("500x500")
words=["school","sleep","braces","cold"]
L1 = Label(root, text="Jumble words")
L1.place(x=160, y=30)
L2 = Label(root, text="", font=("Arial", 14))
L2.place(x=170, y=110)
word=""
def shuffler():
    global word
    word=random.choice(words)
    word_list=list(word)
    random.shuffle(word_list)
    jumbled_word="".join(word_list)
    L2.config(text=jumbled_word)
    print(jumbled_word)
shuffler()
def rw():
    u=(entrybox.get())
    if u == word:
        tkinter.messagebox.showinfo("GOOD","FINALLY jesus christ u r stuuuupid")
    else:
        tkinter.messagebox.showinfo("WRONGGGG","IMAGINE.")
entrybox=Entry(root,width=30)
entrybox.place(x=110,y=60)
B1 = Button(root, text="Submit", command=rw)
B1.place(x=165,y=80)
reset= Button(root,text="Click here for a new word!",command=shuffler )
reset.place(x=135,y=150)
root.mainloop()