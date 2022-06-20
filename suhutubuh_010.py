import colorama
from colorama import Fore
from colorama import Style
import os
os.system("clear")

colorama.init()
print("-------------------------------------------")
T = float(input("Masukkan suhu tubuh anda : ")) 
print("-------------------------------------------")

if T < 36 :
    print(Fore.BLUE + Style.BRIGHT + "Anda mengalami hipotermia." + Style.RESET_ALL)

elif (T <= 37.5) and (T >= 36) :
    print(Fore.GREEN + Style.BRIGHT + "Suhu tubuh anda normal." + Style.RESET_ALL)

elif (T > 37.5) and (T <= 39) :
    print(Fore.YELLOW + Style.BRIGHT + "Anda demam." + Style.RESET_ALL)

else :
    print(Fore.RED + Style.BRIGHT + "Anda mengalami hipertemia." + Style.RESET_ALL)
print("-------------------------------------------")
