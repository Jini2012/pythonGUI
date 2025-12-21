import tkinter
import random 
import tkinter.messagebox
root= tk.Tk()
root.geometry("300x150")
rand=random.randint(0,9)
def cc ():
    guess=int(text.get())
    if guess == rand:
        tkinter.messagebox.showinfo("GOOD","YOU GUESSED IT RIGHT!")
    else:
        tkinter.messagebox.showinfo("SORRY","YOU GUESSED IT WRONG ... sorry not sorry lol.")
label=tk.Label(root,text="pick a 1 digit number").pack(side="top")
text=tk.Entry(root)
text.pack(side="top")

button=tk.Button(root,text="Submit",command=cc).pack(side="top")
root.mainloop()