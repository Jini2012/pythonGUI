import tkinter as tk
from tkinter import ttk

#create a window 
root = tk.Tk()
progress = ttk.Progressbar(root,orient='horizontal',length=100,mode="determinate")

#function resposible to update
def bar():
    import time
    progress['value']=20
    root.update_idletasks()
    time.sleep(1) 

    progress['value']=30
    root.update_idletasks()
    time.sleep(1)

    progress['value']=40
    root.update_idletasks()
    time.sleep(1)  

    progress['value']=50
    root.update_idletasks()
    time.sleep(1) 

    progress['value']=60
    root.update_idletasks()
    time.sleep(1) 

    progress['value']=70
    root.update_idletasks()
    time.sleep(1) 

    progress['value']=80
    root.update_idletasks()
    time.sleep(1) 

    progress['value']=90
    root.update_idletasks()
    time.sleep(1) 

    progress['value']=100

tk.Button(root,text="Start", command=bar).pack(pady=10)
root.mainloop()
