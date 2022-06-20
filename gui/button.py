from tkinter import *

root = Tk()

def myclick() :
    myLabel = Label(root, text="Woah tombolnya berhasil di klik.")
    myLabel.pack()

button1 = Button(root, text="Tekan saya", padx=50, pady=50, command=myclick, fg="white", bg="red")
button1.pack()

root.mainloop()