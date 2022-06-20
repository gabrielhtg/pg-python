from tkinter import *

root = Tk()

nama = Entry(root, width=50)
nama.pack()

def eksekusi() :
    tulisan = Label(root, text=nama.get())
    tulisan.pack()

tombol = Button(root, text="Enter", command=eksekusi, width=50)
tombol.pack()

root.mainloop()