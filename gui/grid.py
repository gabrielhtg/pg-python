from tkinter import *

from pyparsing import col

root = Tk()

tulisan1 = Label(root, text="Halo...")
tulisan2 = Label(root, text="Nama saya Gabriel.")

tulisan1.grid(row=0, column=0)
tulisan2.grid(row=1, column=1)

root.mainloop()