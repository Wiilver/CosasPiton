import keyboard, time, os
from colorama import Fore, Back

def seleccionar_color():
    color = int(input("Esta es la lista de colores que puede seleccionar:\n"
          "1.- Rojo\n"
          "2.- Azul\n"
          "3.- Verde\n"
          "4.- Blanco \n"
          "Opcion : "))-1
    return color

def seleccionar_material(materiales):
    indice = int(input("Esta es la lista de materiales que puedes seleccionar:\n"
                         "1.- #\n"
                         "2.- O\n"
                         "3.- =\n"
                         "Opcion : "))-1
    material = materiales[indice]
    return material

def hacer_mapa(mapa, alto , ancho):
    for i in range (0, alto):
        mapa.append([])
        mapa_colores.append([])
        for j in range(0,ancho):
            mapa[i].append("   ")
            mapa_colores[i].append(3)
            if ((i == 0) | (i == alto - 1)):
                mapa[i][j] = "═══"
            if ((j == 0) | (j == ancho - 1)):
                mapa[i][j] = " ║ "
    mapa[0][0] = " ╔═"
    mapa[alto-1][0] = " ╚═"
    mapa[0][ancho-1] = "═╗ "
    mapa[alto-1][ancho-1] = "═╝ "

def impresion(mapa):
    y = 0
    for i in mapa:
        x = 0
        for j in i:
            print(colores[mapa_colores[y][x]] + j + colores[3].strip(), end="")
            x += 1
        print()
        y += 1
    y= 0
    x = 0
    print(mapa_colores[y][x])

def movimiento( y, x, accion):
    if ((accion == "flecha arriba") | (accion == "w")):
        if y > 1:
            y -= 1
    elif ((accion == "flecha abajo") | (accion == "s")):
        if y < alto-2:
            y += 1
    elif ((accion == "flecha derecha") | (accion == "d")):
        if x < ancho-2:
            x += 1
    elif ((accion == "flecha izquierda") | (accion == "a")):
        if x > 1:
            x -= 1
    return y, x

def comandos():
    print("Esta es una lista de los comandos que tienes disponibles:\n\n"
          "Las teclas WASD, al igual que las flechas sirven para mover tu puntero\n"
          "ENTER sirve para colocar tu objeto en la posicion en la que estas actualmente\n"
          "ESC sirve para salir del programa\n\n"
          "Presione cualquier tecla para salir de este menu")


#Variables

mapa = []
mapa_colores = []
moverse = ("flecha arriba", "flecha abajo", "flecha izquierda", "flecha derecha", "w", "a", "s", "d")

colores= [Fore.RED, Fore.BLUE.strip(), Fore.GREEN, Fore.WHITE]
materiales = [" # ", " O ", " = "]

color = 3
color_anterior = 3
anterior = "   "
material = " O "


#Empieza la cosa

alto = int(input("Escoja lo alto de su lienzo : ")) + 2

ancho = int(input("Escoja lo ancho de su lienzo: ")) + 2

y = alto//2
x = ancho//2

hacer_mapa(mapa, alto, ancho)
impresion(mapa)

while True:
    accion = keyboard.read_key()
    if moverse.__contains__(accion):
        mapa[y][x] = anterior
        mapa_colores [y][x] = color_anterior
        
        y, x = movimiento(y, x, accion)
        
        anterior = mapa[y][x]
        color_anterior = mapa_colores[y][x]
        
        mapa[y][x] = material
        mapa_colores [y][x] = color        
    
    elif accion == "enter":
        anterior = material
        mapa[y][x] = material
        
        color_anterior = color
        mapa_colores [y][x] = color
        
    elif accion == "backspace":
        anterior = "   "
        mapa[y][x] = "   "
        
    elif ((accion == "'")|(accion == "¿")):
        comandos()
        time.sleep(.2)
        keyboard.read_key()
    
    elif accion == "m":
        time.sleep(.2)
        material = seleccionar_material(materiales)
        time.sleep(.2)
    
    elif accion == "c":
        time.sleep(.2)
        color = seleccionar_color()
        time.sleep(.2)
        
    elif accion == "esc":
        break
    
    else:
        print("No se reconocio el comando, presione cualquier tecla para continuar")
        time.sleep(.2)
        keyboard.read_key()
        
    time.sleep(.1)
    os.system("cls")
    impresion(mapa)
os.system("cls")