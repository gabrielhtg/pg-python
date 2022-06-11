import os

os.system('clear')
panjang = input("Masukkan panjang balok : ")
lebar = input("Masukkan lebar balok : ")
tinggi = input("Masukkan tinggi balok : ")


print("\n           Panjang :", panjang)
print("     +---------------------------+")
print("    /|                          /|")
print("   / |                         / |  Tinggi :", tinggi)
print("  +--|------------------------+  |")
print("  |  |                        |  |")
print("  |  +------------------------|--+")
print("  | /                         | /")
print("  |/                          |/ Lebar :", lebar)
print("  +---------------------------+")

for x in range(int(panjang)) :
    print("-", end='  ')

print("\n")