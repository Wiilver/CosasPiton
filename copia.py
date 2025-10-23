import keyboard
import time
import os
from colorama import Fore, Back

color = 0

mapa = []

alto = int(input("Escoja lo alto de su lienzo : ")) + 2

ancho = int(input("Escoja lo ancho de su lienzo: ")) + 2

y = alto//2
x = ancho//2

def seleccionar_color():
    color = int(input("Esta es la lista de colores que puede seleccionar:\n"
          "1.- Rojo\n"
          "2.- Azul\n"
          "3.- Verde\n"
          "Opcion : "))
    return color
def seleccionar_material():
    material = int(input("Esta es la lista de materiales que puedes seleccionar:\n"
                         "1.- #\n"
                         "2.- O\n"
                         "3.- =\n"
                         "Opcion : "))
    return material    
def colorea(color):
    if color == 1:
        print(Fore.RED, end="")
    elif color == 2:
        print(Fore.BLUE, end="")
    elif color == 3:
        print(Fore.GREEN, end="")
def hacer_mapa(mapa, alto , ancho):
    for i in range (0, alto):
        mapa.append([])
        for j in range(0,ancho):
            mapa[i].append("   ")
            if ((i == 0) | (i == alto - 1)):
                mapa[i][j] = "═══"
            if ((j == 0) | (j == ancho - 1)):
                mapa[i][j] = " ║ "
    mapa[0][0] = " ╔═"
    mapa[alto-1][0] = " ╚═"
    mapa[0][ancho-1] = "═╗ "
    mapa[alto-1][ancho-1] = "═╝ "

def impresion(mapa):
    for i in mapa:
        for j in i:
            print(j, end="")
        print()

hacer_mapa(mapa, alto, ancho)
while True:
#Espera hasta que haga algo
    accion = keyboard.read_key()
    if ((accion == "flecha arriba") | (accion == "w")):
        if y > 1:
            mapa[y][x] = "   "
            y -= 1
        time.sleep(.1)
        os.system("cls")
    elif ((accion == "flecha abajo") | (accion == "s")):
        if y < alto-2:
            
            mapa[y][x] = "   "
            y += 1
        time.sleep(.1)
        os.system("cls")
    elif ((accion == "flecha derecha") | (accion == "d")):
        if x < ancho-2:
            mapa[y][x] = "   " 
            x += 1
        time.sleep(.1)
        os.system("cls")
    elif ((accion == "flecha izquierda") | (accion == "a")):
        if x > 1:
            mapa[y][x] = "   " 
            x -= 1
        time.sleep(.1)
        os.system("cls")
    elif accion == "esc":
        break
    else:
        print("No se reconocio el comando")
        time.sleep(.1)
    mapa[y][x] = " O "
    impresion(mapa)
os.system("cls")