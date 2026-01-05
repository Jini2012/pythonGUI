from tkinter import *
import random
root= Tk()
root.geometry("300x200")
words=["school","sleep","braces","cold"]
def shuffler():
    word=random.choice(words)
    word_list=list(word)
    random.shuffle(word_list)
    jumbled_word="".join(word_list)
    print(jumbled_word)
shuffler()
L1=Label(root,text="Jumble words")
L1.place(x=160,y=30)
L2=Label(root,text="")
L2.place(x=170,y=110)
entrybox=Entry(root,width=30)
entrybox.place(x=110,y=60)
B1=Button(root,text="Submit",)
B1.place(x=165,y=80)
root.mainloop()