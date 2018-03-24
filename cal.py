from calendar import monthcalendar
from os import system
from time import sleep
from colorama import Fore, Style, Back, Cursor, init

init(autoreset=True)

anchor = 36
system("clear")
print("\n")
sem = ["Lu","Ma","Mi","Ju","Vi","Sa","Do"]
mes = monthcalendar(2018,3)
print(Back.WHITE+Style.DIM+Fore.BLACK+"="*anchor)
print(Back.WHITE+Style.DIM+Fore.GREEN+(">MARZO 2018<".center(anchor,"-")))
print(Back.WHITE+Fore.BLACK+"="*anchor)
print(Back.WHITE+Style.DIM+Fore.RED+(Fore.BLACK+Style.DIM+"| "+Fore.RED+(Fore.BLACK+" | "+Fore.RED).join(sem)+Fore.BLACK+Style.DIM+" |").center(anchor))
print(Back.WHITE+Fore.BLACK+"="*anchor)

for i in range(len(mes)):
    for j in range(len(mes[i])):
        if mes[i][j] == 0:
            mes[i][j] = "--"
        elif mes[i][j]>0 and mes[i][j]<10:
            mes[i][j] = "0"+str(mes[i][j])
        else:
            mes[i][j] = str(mes[i][j])
    print(Back.WHITE+Style.DIM+Fore.BLACK+("| "+(Fore.BLACK+" | "+Fore.BLACK).join(mes[i])+" |").center(anchor))
    print(Back.WHITE+Fore.BLACK+"-"*anchor)

print("\n")

