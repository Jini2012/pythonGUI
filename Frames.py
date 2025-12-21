import tkinter as tk
window = tk.Tk()
window.geometry("300x150")
window_label=tk.Label(window,text="Choose dessert")
window_label.pack()

#first frame
frame = tk.Frame(window)
frame.pack()

#buttom frame
bottom_frame=tk.Frame(window)
bottom_frame.pack(side=tk.BOTTOM)

#make the buttons
b1=tk.Button(frame , text="Dark Choco" , bg="beige")
b1.pack(side="left")
b2=tk.Button(frame,text="Choco",fg="brown",bg="yellow")
b2.pack(side="left")

window.mainloop()