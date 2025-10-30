from colorama import Fore, Style, Back
import keyboard
while True:
    if keyboard.is_pressed("enter"):
        print("Presionaste enter")
    elif keyboard.is_pressed("spacebar"):
        break
print(Back.RED, end="")
print(Fore.YELLOW, end = "")
print("Buenas tardes")
