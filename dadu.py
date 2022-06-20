import os
import random
os.system('clear')

while True :
    yesno = input("Kocok dadu? (y/n) : ")

    if (yesno == "y") or (yesno == "Y") :
        print(random.randint(1, 6))

    else :
        break

