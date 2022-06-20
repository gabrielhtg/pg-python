from tkinter import *

root = Tk()
root.title("GCalc")
root['bg'] = '#242424'

# Tempat fungsi diletakkan
def myclick(number):
    layar.insert(END, number)
    
def myclear() :
    layar.delete(0, END)

def samadengan():
    hasil = str(eval(layar.get()))
    layar.delete(0, END)
    layar.insert(0, hasil)
    
# Desain UI

layar = Entry(root, width=43, borderwidth=5, bg="#454545", fg='white', font=('FiraMono', 12))
layar.grid(row=0, column=0, columnspan=4, pady=10, ipady=10)

tombol1 = Button(root, width=7, height=2, text="1", command=lambda: myclick(1), bg="#454545", fg="white", font=('FiraMono', 12))
tombol2 = Button(root, width=7, height=2, text="2", command=lambda: myclick(2), bg="#454545", fg="white", font=('FiraMono', 12))
tombol3 = Button(root, width=7, height=2, text="3", command=lambda: myclick(3), bg="#454545", fg="white", font=('FiraMono', 12))
tombol4 = Button(root, width=7, height=2, text="4", command=lambda: myclick(4), bg="#454545", fg="white", font=('FiraMono', 12))
tombol5 = Button(root, width=7, height=2, text="5", command=lambda: myclick(5), bg="#454545", fg="white", font=('FiraMono', 12))
tombol6 = Button(root, width=7, height=2, text="6", command=lambda: myclick(6), bg="#454545", fg="white", font=('FiraMono', 12))
tombol7 = Button(root, width=7, height=2, text="7", command=lambda: myclick(7), bg="#454545", fg="white", font=('FiraMono', 12))
tombol8 = Button(root, width=7, height=2, text="8", command=lambda: myclick(8), bg="#454545", fg="white", font=('FiraMono', 12))
tombol9 = Button(root, width=7, height=2, text="9", command=lambda: myclick(9), bg="#454545", fg="white", font=('FiraMono', 12))
tombol0 = Button(root, width=7, height=2, text="0", command=lambda: myclick(0), bg="#454545", fg="white", font=('FiraMono', 12))
tombol_titik = Button(root, width=7, height=2, text=".", command=lambda: myclick("."), bg="#454545", fg="white", font=('FiraMono', 12))
tombol_sd = Button(root, width=7, height=2, text="=", command=samadengan, bg="#454545", fg="white", font=('FiraMono', 12))
tombol_tambah = Button(root, width=7, height=2, text="+", command=lambda: myclick("+"), bg="#454545", fg="white", font=('FiraMono', 12))
tombol_kurang = Button(root, width=7, height=2, text="-", command=lambda: myclick("-"), bg="#454545", font=('FiraMono', 12), fg='white')
tombol_kali = Button(root, width=7, height=2, text="᰽", command=lambda: myclick("*"), bg="#454545", fg="white", font=('FiraMono', 12))
tombol_bagi = Button(root, width=7, height=2, text="÷", command=lambda: myclick("/"), bg="#454545", fg="white", font=('FiraMono', 12))
tombol_clear = Button(root, width=40, height=2, text="Clear", command=myclear, bg="#454545", fg="white", font=('FiraMono', 12))


tombol1.grid(row=3, column=0, pady=1)
tombol2.grid(row=3, column=1, pady=5)
tombol3.grid(row=3, column=2, pady=5)
tombol4.grid(row=2, column=0)
tombol5.grid(row=2, column=1)
tombol6.grid(row=2, column=2)
tombol7.grid(row=1, column=0, pady=5)
tombol8.grid(row=1, column=1, pady=5)
tombol9.grid(row=1, column=2, pady=5)
tombol0.grid(row=4, column=0)
tombol_titik.grid(row=4, column=1)
tombol_sd.grid(row=4, column=2)
tombol_tambah.grid(row=4, column=3)
tombol_kali.grid(row=2, column=3)
tombol_kurang.grid(row=3, column=3)
tombol_bagi.grid(row=1, column=3)
tombol_clear.grid(row=5, column=0, columnspan=4, pady=5)

root.mainloop()