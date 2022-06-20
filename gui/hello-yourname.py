from tkinter import *

root = Tk()

nama = Entry(root, width=50)
nama.pack()
nama.insert(0, "Enter your name")

def halo() :
    greeting = "Hello", nama.get()
    label1 = Label(root, text=greeting)
    label1.pack()
    
tombol = Button(root, text="Enter", command=halo)
tombol.pack()

root.mainloop()