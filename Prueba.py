from colorama import Fore, Style, Back
import keyboard

azul = [1, 2, 3, 4]

def azuleando(lista):
    lista[0] = 10
    print(lista[0])
    
azuleando(azul)
print(azul[0])