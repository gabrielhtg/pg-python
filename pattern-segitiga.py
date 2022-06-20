import os

os.system('clear')

n = int(input("Masukkan panjang alas segitiga : "))

for i in range(n) :
    print((n-i-1) * " ", end="")
    
    for j in range(i+1) :
        print("b", end=" ")
    
    print()