import keyboard, time, os
from colorama import Fore, Back

#Falta que agregues los otros tipos de objeto, que reinicies la posicion al pasar al modo de prueba

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
        mapa_caracteristicas.append([])
        mapa_colores.append([])
        mapa_fondo.append([])
        for j in range(0,ancho):
            mapa[i].append("   ")
            mapa_caracteristicas[i].append("")
            mapa_colores[i].append(3)
            mapa_fondo[i].append(6)
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
            print(fondos[mapa_fondo[y][x]], end="")
            print(colores[mapa_colores[y][x]], end="")
            print(j,end="")
            x += 1
        print()
        y += 1
    y= 0
    x = 0

def movimiento(y, x, accion):
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

def movimiento_prueba( y, x, accion):
    if ((accion == "flecha arriba") | (accion == "w")):
        if y > 1:
            if mapa_caracteristicas[y-1][x] == "pared":
                print("No puedes moverte en esa direccion, hay algo que te detiene")
                time.sleep(.1)
                keyboard.read_event()
            else:
                y -= 1
    elif ((accion == "flecha abajo") | (accion == "s")):
        if y < alto-2:
            if mapa_caracteristicas[y+1][x] == "pared":
                print("No puedes moverte en esa direccion, hay algo que te detiene")
                time.sleep(.1)
                keyboard.read_event()
            else:
                y += 1
    elif ((accion == "flecha derecha") | (accion == "d")):
        if x < ancho-2:
            if mapa_caracteristicas[y][x+1] == "pared":
                print("No puedes moverte en esa direccion, hay algo que te detiene")
                time.sleep(.1)
                keyboard.read_event()
            else:
                x += 1
    elif ((accion == "flecha izquierda") | (accion == "a")):
        if x > 1:
            if mapa_caracteristicas[y][x-1] == "pared":
                print("No puedes moverte en esa direccion, hay algo que te detiene")
                time.sleep(.1)
                keyboard.read_event()
            else:
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

def nuevo_texto():
    while True:
            nombre = input("Para introducir un texto, primero introduce el titulo del mismo : ")
            if not nombre:
                print("Debes de poner por lo mismo un caracter, por favor, intentalo de nuevo")
            else:
                break
    while True:
        contenido = input("Ahora introduce el texto que ira dentro : ")
        if not contenido:
            print("Necesiitas poner algo dentro, por favor, intentalo de nuevo")
        else:
            break
    return nombre, contenido

def tipo_material():
    print("Presione ENTER para continuar")
    while True:
        while True:
            try:
                opcion = int(input("Seleccione el tipo de material que quiere usar:\n"
                    "1.- Pared\n"
                    "2.- Texto\n"
                    "3.- Npc\n"
                    "4.- Enemigo\n"
                    "5.- Nulo\n"
                    "Tipo : "))
                break
            except:
                print("Solo se admiten valores numericos, por favor, intentelo de nuevo")
        if ((opcion < 1)|(opcion > 5)):
            print("Los valores deben de ir de 1 a 5, por favor, intentelo de nuevo")
        else:
            break
    if opcion == 1:
        return "pared"
    elif opcion == 2:
        if not textos:
            while True:
                crear = input("Parece que no tienes textos hechos, quieres crear uno (S/N)?: ")
                if crear == "S":
                    nombre, contenido = nuevo_texto()
                    textos[nombre] = contenido
                    return f"texto_{nombre}"
                elif crear == "N":
                    print(end="")
                    break
                else:
                    print("Favor de utilizar una S o una N como respuesta")
        else:
            while True:
                crear = input("Quiere crear un texto nuevo o utilizar uno antiguo (N/A)?: ")
                if crear == "N":
                    nombre, contenido = nuevo_texto()
                    textos[nombre] = contenido
                    return f"texto_{nombre}"
                elif crear == "A":
                    print("Esta es una lista de los textos que ya tienes hechos:")
                    contador = 1
                    for i in textos.keys():
                        print(f"{contador}.- {i}")
                    opcion = input("Seleccione el titulo del texto que quiera reutilizar : ")
                    if textos.keys().__contains__(opcion):
                        return f"texto_{opcion}"
                else:
                    print("Por favor, utilizar N o A como respuesta")
    elif opcion == 3:
        return "npc"
    elif opcion == 4:
        return "enemigo"
    elif opcion == 5:
        return ""

#Variables

mapa = []
mapa_fondo= []
mapa_colores = []
mapa_caracteristicas = []
# "pared", "texto", "npc", "enemigo", ""
moverse = ("flecha arriba", "flecha abajo", "flecha izquierda", "flecha derecha", "w", "a", "s", "d")

fondos = [Back.RED, Back.BLUE, Back.GREEN, Back.WHITE, Back.YELLOW, Back.CYAN, Back.BLACK, Back.MAGENTA]
colores= [Fore.RED, Fore.BLUE, Fore.GREEN, Fore.WHITE, Fore.YELLOW, Fore.CYAN, Fore.BLACK, Fore.MAGENTA]

lineas_simples = [" ┌─","─┘ ","─┐ ", " └─", "─┴─", "─┬─", " ├─", "───", "─┼─", "─┤ ", " │ "]
lineas_dobles = ["═╣ ", " ║ ", "═╗ ", "═╝ ", " ╚═", " ╔═", "═╩═", "═╦═", " ╠═", "═══", "═╬═"]
lineas = [lineas_simples, lineas_dobles]

texturas = ["░░░", "▒▒▒", "▓▓▓", " ░ ", " ▒ ", " ▓ "]

bloques = ["███", " █ "," ▄ ", " ▀ ", " ■ "]

otros = [" ≡ ", " ¦ ", " ¤ ", " O "]

del_usuario = []

textos = {}

materiales = [lineas, texturas, bloques, otros, del_usuario]

tipo = ""
fondo = 6
color = 3
fondo_anterior = 6
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
    textos.update()
    print(textos)
    accion = keyboard.read_key().lower()
    os.system("cls")
    
    if prueba:
        if moverse.__contains__(accion):
            mapa[y][x] = anterior
            mapa_colores [y][x] = color_anterior
            mapa_fondo [y][x] = fondo_anterior
            
            y, x = movimiento_prueba(y, x, accion)
            
            anterior = mapa[y][x]
            fondo_anterior = mapa_fondo[y][x]
            color_anterior = mapa_colores[y][x]
            
            mapa[y][x] = material
            mapa_fondo [y][x] = fondo
            mapa_colores [y][x] = color
            
            if mapa_caracteristicas[y][x].startswith("texto"):
                clave = mapa_caracteristicas[y][x].split("_")
                input("...")
                input(f"\n{textos[mapa_caracteristicas[y][x].split("_")[1]]}")
            
        elif accion == "q":
            prueba = False
            
    else:
        if moverse.__contains__(accion):
            mapa[y][x] = anterior
            mapa_colores [y][x] = color_anterior
            mapa_fondo [y][x] = fondo_anterior
            
            y, x = movimiento(y, x, accion)
            
            anterior = mapa[y][x]
            fondo_anterior = mapa_fondo[y][x]
            color_anterior = mapa_colores[y][x]
            
            mapa[y][x] = material
            mapa_fondo [y][x] = fondo
            mapa_colores [y][x] = color        
        
        elif accion == "enter":
            anterior = material
            mapa[y][x] = material
            
            color_anterior = color
            mapa_colores [y][x] = color
            
            fondo_anterior = fondo
            mapa_fondo [y][x] = fondo
            
            mapa_caracteristicas[y][x] = tipo
            
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
            prueba = True
            
        elif accion == "t":
            tipo = tipo_material()
            
        elif accion == "f":
            fondo = seleccionar_color()
            
        elif accion == "esc":
            break
        
        else:
            print("No se reconocio el comando, presione cualquier tecla para continuar")
            keyboard.read_key()
        
    time.sleep(.1)
    os.system("cls")
    if not prueba:
        print(f"El material que esta usando tiene tipo {tipo}\n")
        print(f"El tipo de esta casilla es {mapa_caracteristicas[y][x]}")
    impresion(mapa)
os.system("cls")