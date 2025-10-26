import keyboard, time, os
from colorama import Fore, Back

##Te deje la funcionm puesta, com el prieba puesto

#Ocupas hacer que se pueda cambiar el color del fondo

os.system("")

def seleccionar_color():
    input("Presione ENTER para continuar...")
    while True:
        while True:
            try:
                color = int(input("Esta es la lista de colores que puede seleccionar:\n"
                    "1.- Rojo\n"
                    "2.- Azul\n"
                    "3.- Verde\n"
                    "4.- Blanco \n"
                    "5.- Amarillo\n"
                    "6.- Cyan\n"
                    "7.- Negro\n"
                    "8.- Magenta\n"
                    "Opcion : "))-1
                break
            except:
                print("Hubo un error, recuerda que solo puedes ingresar numeros")
        if ((color < 0)|(color > 7)):
            print("Hermano, el numero debe de estar entre el 1 y el 8, intentalo nuevamente")
        else:
            break
    input("Presione ENTER para salir...")
    
    return color

def seleccionar_material(materiales):
    input("Presione ENTER para continuar...")
    while True:
        while True:
            try:
                indice = int(input("Estas son las categorias de materiales disponibles \n"
                                "1.- Lineas\n"
                                "2.- Texturas \n"
                                "3.- Bloques\n"
                                "4.- Otros\n"
                                "5.- Del usuario\n"
                                "Opcion : "))-1
                break
            except:
                print("Hermano, solo puedes ingresar numeros, por favor intentalo de nuevo")
        if ((indice < 0)|(indice > 4)):
            print("Hermano, el numero debe de estar entre 1 y 5, por favor intentalo nuevamente")
        else:
            break
    if indice == 4:
        if len(materiales[4]) == 0:
            print("Hermano, esta lista esta vacia de momento")
        else:
            print("Estos son los materiales que tienes disponibles")
            contador = 1
            for i in materiales[4]:
                print(f"{contador}.- {i}")
                contador +=1
            print()
            while True:
                while True:
                    try:
                        indice = int(input("Material : "))-1
                        break
                    except:
                        print("Hermano, solo puedes ingresar numeros, por favor intentalo nuevamente")
                if ((indice < 0)|(indice > len(materiales[4]))):
                    print(f"Hermano, el indice debe de estar entre 1 y {len(materiales[4])}, por favor intentalo nuevamente")
                else:
                    break
            material = materiales[4][indice]
            input("Presione ENTER para salir...")
            return material
    elif indice == 0:
        while True:
            while True:
                try:
                    indice = int(input("Las lineas tienen dos subcategorias:\n"
                                    "1.- Lineas simples\n"
                                    "2.- Lineas dobles\n"
                                    "Favor de seleccionar que opcion desea : "))-1
                    break
                except:
                    print("Hermano, solamente se admiten numeros, por favor intentalo nuevamente")
            if ((indice < 0)|(indice > 1)):
                print("Hermano, solo se admiten los valores 1 y 2, por favor intentalo nuevamente")
            else:
                break
        contador = 1
        for i in materiales[0][indice]:
            print(f"{contador}.- {i}")
            contador +=1
        print()
        while True:
            while True:
                try:
                    indice2 = int(input("Material : "))-1
                    break
                except:
                    print("Hermano, solo se admiten numeros, por favor intentalo nuevamente")
            if ((indice2 < 0)|(indice2 > len(materiales[0][indice]))):
                print(f"Hermano, el indice debe de estar entre 1 y {len(materiales[0][indice])}, por favor intentalo nuevamente")
            else:
                break
        material = materiales[0][indice][indice2]
        input("Presione ENTER para salir...")
        return material
    else:
        contador = 1
        for i in materiales[indice]:
            print(f"{contador}.- {i}")
            contador += 1
        print()
        while True:
            while True:
                try:
                    indice2 = int(input("Material : "))-1
                    break
                except:
                    print("Hermano, solo se admiten numeros, por favor intentalo nuevamente")
            if ((indice2 < 0)|(indice2 > len(materiales[indice]))):
                print(f"Hermano, el indice debe de estar entre 1 y {len(materiales[indice])}, por favor, intentalo de nuevo")
            else:
                break
        material = materiales[indice][indice2]
        input("Presione ENTER para salir...")
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

def movimiento_prueba(y, x, accion):
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
          "ESC sirve para salir del programa\n")
    input("Presione ENTER para salir...")
    
def nuevo_material():
    input("Presione ENTER para iniciar...")
    while True:
        nuevo = input("Introduzca el material que quiera agregar al sistema\n"
                  "Debe de tener en cuenta que necesita tener 3 o 1 caracter de largo\n"
                  "Si es uno solo, el caracter se centrara y se rellenara con espacios:\n"
                  "Nuevo material : ")
        if len(nuevo) == 3:
            break
        elif len(nuevo) == 1:
            nuevo = " " + nuevo + " "
            break
        else:
            print("La longitud registrada del material no fue ni de 3 ni de 1 caracter, intentelo de nuevo")
    input("Presione ENTER para salir...")
    return nuevo

#Variables

mapa = []
mapa_colores = []
moverse = ("flecha arriba", "flecha abajo", "flecha izquierda", "flecha derecha", "w", "a", "s", "d")

colores= [Fore.RED, Fore.BLUE, Fore.GREEN, Fore.WHITE, Fore.YELLOW, Fore.CYAN, Fore.BLACK, Fore.MAGENTA]

lineas_simples = [" ┌─","─┘ ","─┐ ", " └─", "─┴─", "─┬─", " ├─", "───", "─┼─", "─┤ ", " │ "]
lineas_dobles = ["═╣ ", " ║ ", "═╗ ", "═╝ ", " ╚═", " ╔═", "═╩═", "═╦═", " ╠═", "═══", "═╬═"]
lineas = [lineas_simples, lineas_dobles]

texturas = ["░░░", "▒▒▒", "▓▓▓", " ░ ", " ▒ ", " ▓ "]

bloques = ["███", " █ "," ▄ ", " ▀ ", " ■ "]

otros = [" ≡ ", " ¦ ", " ¤ ", " O "]

del_usuario = []

materiales = [lineas, texturas, bloques, otros, del_usuario]

color = 3
color_anterior = 3
anterior = "   "
material = " O "
prueba = False


#Empieza la cosa
while True:
    try:
        alto = int(input("Escoja lo alto de su lienzo : ")) + 2
        ancho = int(input("Escoja lo ancho de su lienzo: ")) + 2
        break
    except:
        print("Hermano, solo se admiten numeros, por favor intentalo nuevamente")

input("Presione ENTER para continuar")

y = alto//2
x = ancho//2

hacer_mapa(mapa, alto, ancho)
impresion(mapa)

while True:
    accion = keyboard.read_key()
    os.system("cls")

    if moverse.__contains__(accion):
        if prueba:
            
        
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
    
    elif accion == "m":
        material = seleccionar_material(materiales)
    
    elif accion == "n":
        del_usuario.append(nuevo_material())
    
    elif accion == "c":
        color = seleccionar_color()
        
    elif accion == "q":
        if prueba:
            prueba = False
        else:
            prueba = True
        
    elif accion == "esc":
        break
    
    else:
        print("No se reconocio el comando, presione cualquier tecla para continuar")
        keyboard.read_key()
        
    time.sleep(.1)
    os.system("cls")
    impresion(mapa)
os.system("cls")