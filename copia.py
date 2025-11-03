import keyboard, time, os
from colorama import Fore, Back

#Falta que enemigos, debes de hacerlo mejor, con cls, inputs, sleeps y tal
#Hacer que la cara vacia se quede vacia

#Variables

personaje = [" O ", 3]

cara_vacia = []

mapa = []
mapa_fondo= []
mapa_colores = []
mapa_caracteristicas = []
# "pared", "texto", "npc", "enemigo", "", "inicio", "interaccion"

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

materiales = [lineas, texturas, bloques, otros, del_usuario]


npcs_caras = {}
textos = {}
conversaciones = {}

tipo = ""

material = " O "
anterior = "   "

fondo = 6
fondo_anterior = 6

color = 3
color_anterior = 3

inicio = 0


prueba = False


def crear_expresion_npc(cara):
    os.system("cls")
    input("Crearemos una expresion para mostrar en una conversacion...\n")
    while True:
        nombre_npc = input("Primero que nada, introduzca el nombre de su expresion : ")
        if not nombre_npc:
            print("Necesita tener un nombre, por favor intentelo de nuevo\n")
        else:
            break
    return cara_npc(material, cara), nombre_npc
    
def cara_npc(material, cara):
    y = 3
    x = 3
    anterior = "   "
    while True:
        accion = keyboard.read_key().lower()
        if moverse.__contains__(accion):
            cara[y][x] = anterior
            
            y, x = movimiento(y, x, accion, 5, 5)
            
            anterior = cara[y][x]
            cara[y][x] = material
            
        elif accion == "enter":
            anterior = material
            cara[y][x] = material
        
        elif accion == "backspace":
            cara[y][x] = "   "
            anterior = "   "
        
        elif accion == "m":
            material = seleccionar_material(materiales)
            
        elif accion == "esc":
            time.sleep(.1)
            os.system("cls")
            input("...")
            while True:
                opcion = input("Seguro que así quiere que se vea el npc? Esta configuracion no se podra cambiar (S/N) : ").upper().strip()
                if opcion == "S":
                    return cara
                elif opcion != "N":
                    print("\nSolo se admite S o N como respuesta, por favor, vuelve a intentarlo\n")
                else:
                    break
        
        time.sleep(.1)
        os.system("cls")
        
        impresion_cara(cara)
    
def crear_personaje():
    input("Crearemos un personaje para el usuario\n")
    while True:
        input("...")
        print("Considere que solo pueden usarse 1 o 3 caracteres, los espacios cuentan")
        personaje = input("Introduzca los caracteres que conformen el personaje del jugador : ")
        if not personaje:
            print("Por favor, intentelo de nuevo")
        elif len(personaje) == 1:
            personaje = " " + personaje + " "
            break
        elif len(personaje) == 3:
            break
        else:
            print("La longitud no coincide ni con 1 ni con 3 caracteres, por favor intentelo de nuevo")
    print("Ahora seleccionaras el color del personaje")
    color = seleccionar_color()
    
    return personaje, color
    
def seleccionar_color():
    input("Presione ENTER para continuar...")
    while True:
        while True:
            try:
                opcion = int(input("Esta es la lista de colores que puede seleccionar:\n"
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
        if ((opcion < 0)|(opcion > 7)):
            print("Hermano, el numero debe de estar entre el 1 y el 8, intentalo nuevamente")
        else:
            break
    input("Presione ENTER para salir...")
    
    return opcion

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

def hacer_cara():
    cara_vacia.clear()
    for i in range (0,7):
        cara_vacia.append([])
        for j in range (0,7):
            cara_vacia[i].append("   ")
            if ((i == 0)|(i == 6)):
                cara_vacia[i][j] = "═══"
            if ((j == 0)|(j == 6)):
                cara_vacia[i][j] = " ║ "
    cara_vacia[0][0] = " ╔═"
    cara_vacia[6][0] = " ╚═"
    cara_vacia[0][6] = "═╗ "
    cara_vacia[6][6] = "═╝ "
    return cara_vacia
    
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

def impresion_cara(cara):
    for i in cara:
        for j in i:
            print(j, end="")
        print()

def impresion(mapa):
    y = 0
    for i in mapa:
        x = 0
        for j in i:
            print(fondos[mapa_fondo[y][x]], end="")
            print(colores[mapa_colores[y][x]] + j, end="")
            x += 1
        print()
        y += 1
    y= 0
    x = 0

def movimiento(y, x, accion, altura, gordeza):
    if ((accion == "flecha arriba") | (accion == "w")):
        if y > 1:
            y -= 1
    elif ((accion == "flecha abajo") | (accion == "s")):
        if y < altura:
            y += 1
    elif ((accion == "flecha derecha") | (accion == "d")):
        if x < gordeza:
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
          "Las teclas WASD, al igual que las flechas, sirven para mover tu puntero\n"
          "ENTER sirve para colocar tu objeto en la posicion en la que estas actualmente\n"
          "BACKSPACE sirve para borrar el la casilla actual, también resetea su color, tipo y fondo\n\n"
          "M sirve para escoger el material que usaras\n"
          "N sirve para crear un nuevo material\n"
          "T sirve para escoger el tipo/propiedad del material\n"
          "C sirve para escoger el color del material\n"
          "F sirve para escoger el color del fondo del material\n\n"
          "Q sirve para cambiar entre el modo de prueba y el editor\n\n"
          "ESC sirve para salir del programa (solo lo puedes hacer desde el editor)\n")
    input("Presione ENTER para salir...")
    
def nuevo_material():
    input("Haremos un nuevo material...\n")
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

def nueva_conversacion():
    os.system("cls")
    input("Crearemos una conversacion...\n")
    while True:
        nombre = input("Por favor, pongale un nombre a la conversacion : ")
        if not nombre:
            print("Hermano, pon algo minimo")
        else:
            break
    print()
    conversacion = []
    contador = 1
    while True:
        for i in npcs_caras.keys():
            print(f"{contador}.- {i}")
            contador += 1
        contador = 1
        try:
            escoger_cara = input("Esta es una lista de las expresiones que has creado, escoge cual quieras usar : ")
            print()
            if npcs_caras.keys().__contains__(escoger_cara):
                for i in textos.keys():
                    print(f"{contador}.- {i}")
                    contador += 1
                while True:
                    try:
                        
                        escoger = input("Esta es una lista de los textos que has creado, escoge cual quieras usar : ")
                        print()
                        if not textos.keys().__contains__(escoger):
                            print("Respondiste con una clave que no existe, por favor, intentalo de nuevo")
                        elif not escoger:
                            print("Hermanito, por favor, minimo contesta algo")
                        else:
                            conversacion.append([escoger_cara, escoger])
                            while True:
                                escoger = input("Deseas agregar otra viñeta (S/N) : ").upper().strip()
                                if ((escoger != "S")&(escoger != "N")):
                                    print("Hermano, solo se admiten S o N como respuestas, por favor intentalo nuevamente")
                                else:
                                    break
                        if escoger == "N":
                            return conversacion, nombre
                        else:
                            break
                    except:
                        print("Hermano, hubo un error con el dato que me tiraste, por favor, intentalo de nuevo")
            elif not escoger_cara:
                print("Hermanito, por favor, minimo contesta algo")
            else:
                print("La clave que introdujiste no coincide con ninguna que te hubieran dado, por favor, intentalo nuevamente")
        except:
            print("Hermano, hubo un error con el dato que me tiraste, por favor, intentalo de nuevo")
        
def nuevo_texto():
    os.system("cls")
    input("Crearemos un texto...\n")
    contenido = []
    while True:
            nombre = input("Para crear un texto, primero introduce el titulo del mismo : ")
            if not nombre:
                print("Debes de poner por lo mismo un caracter, por favor, intentalo de nuevo")
            else:
                break
    while True:
        letras = input("Ahora introduce el texto : ")
        if not letras:
            print("Necesiitas poner algo dentro, por favor, intentalo de nuevo")
        else:
            contenido.append(letras)
            while True:
                opcion = input("Quieres agregar otra linea de texto (S/N)? : ").upper()
                if ((opcion!="S")&(opcion!="N")):
                    print("Por favor, solo se admite S o N como respuesta, escriba bien mi estimado")
                else:
                    break
            if opcion == "N":
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
                    "6.- Punto de inicio\n"
                    "7.- Interaccion\n"
                    "Tipo : "))
                break
            except:
                print("Solo se admiten valores numericos, por favor, intentelo de nuevo")
        if ((opcion < 1)|(opcion > 7)):
            print("Los valores deben de ir de 1 a 5, por favor, intentelo de nuevo")
        else:
            break
    if opcion == 1:
        return "pared"
    elif ((opcion == 2)|(opcion == 7)):
        if not textos:
            while True:
                crear = input("Parece que no tienes textos hechos, quieres crear uno (S/N)?: ")
                if crear == "S":
                    nombre, contenido = nuevo_texto()
                    textos[nombre] = contenido
                    if opcion == 2:
                        return f"texto_{nombre}"
                    else:
                        return f"interaccion_{nombre}"
                elif crear == "N":
                    break
                else:
                    print("Favor de utilizar una S o una N como respuesta")
        else:
            while True:
                crear = input("Quiere crear un texto nuevo o utilizar uno antiguo (N/A)?: ")
                if crear == "N":
                    nombre, contenido = nuevo_texto()
                    textos[nombre] = contenido
                    if opcion == 2:
                        return f"texto_{nombre}"
                    else:
                        f"interaccion_{nombre}"
                elif crear == "A":
                    print("Esta es una lista de los textos que ya tienes hechos:")
                    contador = 1
                    for i in textos.keys():
                        print(f"{contador}.- {i}")
                    opcion = input("Seleccione el titulo del texto que quiera reutilizar : ")
                    if textos.keys().__contains__(opcion):
                        if opcion == 2:
                            return f"texto_{opcion}"
                        else:
                            f"interaccion_{opcion}"
                else:
                    print("Por favor, utilizar N o A como respuesta")
    
    elif opcion == 3:
        print()
        if not npcs_caras:
            while True:
                hacer = input("Parece que aún no tienes ninguna expresion hecha, deseas crear una (S/N)? : ").upper().strip()
                if hacer == "S":
                    print("\nPrimero crearas la expresion en si, es como al hacer un mapa, pero el único comando activo es M, ENTER y BACKSPACE")
                    input("Cuando estes contento con como se ve presiona ESC, si entendiste esto, presiona ENTER para continuar...")
                    print()
                    crear_expresion_npc()
                    print()
                    break
                elif hacer == "N":
                    return ""
                else:
                    print("Solo puedes usar S o N como respuesta, por favor, contesta bien")
        if not textos:
            os.system("cls")
            while True:
                hacer = input("Para crear un npc necesitas tener minimo un texto creado, deseas hacer uno nuevo (S/N)? : ").upper().strip()
                if hacer == "S":
                    print()
                    nombre, contenido = nuevo_texto()
                    textos[nombre] = contenido
                    print()
                    break
                elif hacer == "N":
                    return ""
                else:
                    print("\nPor favor, esfuercese para contestar con S o N solamente e intentelo de nuevo\n")
        if not conversaciones:
            os.system("cls")
            while True:
                hacer = input("Para definir un npc es necesario que tengas una conversacion creada, deseas hacer una (S/N)? : ").upper().strip()
                if hacer == "S":
                    chat, nombre = nueva_conversacion()
                    conversaciones[nombre] = chat
                    return f"npc_{nombre}"
                elif hacer == "N":
                    break
                else:
                    print("\nPor favor, esfuercese para contestar con S o N solamente e intentelo de nuevo\n")
        else:
            os.system("cls")
            while True:
                hacer = input("Parece que ya tiene alguna conversacion, desea usar una antigua o crear una nueva(N/A)? : ").upper().strip()
                if hacer == "N":
                    chat, nombre = nueva_conversacion()
                    conversaciones[nombre] = chat
                    return f"npc_{nombre}"
                elif hacer == "A":
                    while True:
                        os.system("cls")
                        contador = 1
                        for i in conversaciones.keys():
                            print(f"{contador}.- {i}")
                            contador += 1
                        print()
                        hacer = input("Esta es una lista de las conversaciones que tienes creadas, escribe el nomrbe de la que quieras usar : ")
                        if conversaciones.keys().__contains__(hacer):
                            return f"npc_{hacer}"
                        else:
                            print("Parece que lo que introdujiste no concuerda con el nombre de ninguna conversacion, por favor, intentalo nuevamente")
                    
    elif opcion == 4:
        return "enemigo"
    elif opcion == 5:
        return ""
    elif opcion == 6:
        return "inicio"
    
def mostrar_conversacion():
    input(...)
    clave = mapa_caracteristicas[y][x].split("_")[1]
    largo = len(conversaciones[clave])
    for i in range(0, largo):
        print (conversaciones[clave][i][0])
        for j in npcs_caras[conversaciones[clave][i][0]]:
            for k in j:
                print(k, end="")
            print()
        for k in textos[conversaciones[clave][i][1]]:
            input(f"{k}\n") 

def leer():
    clave = mapa_caracteristicas[y][x].split("_")[1]
    input("...")
    for i in textos[clave]:
        input(f"{i}\n")

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
punto_inicio = [y,x]

hacer_mapa(mapa, alto, ancho)
hacer_cara()

impresion(mapa)

while True:
    print(cara_vacia)
    textos.update()
    print(npcs_caras)
    print(textos)
    accion = keyboard.read_key().lower()
    
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
                leer()
                
            elif mapa_caracteristicas[y][x].startswith("npc"):
                mostrar_conversacion()
                
            elif mapa_caracteristicas[y][x].startswith("interaccion"):
                print("Tu personaje esta pensando algo, presiona ENTER para escucharlo")
                time.sleep(.1)
                pensar = keyboard.read_key()
                if pensar == "enter":
                    leer()
                    
            
        elif accion == "q":
            prueba = False
            
    else:
        if moverse.__contains__(accion):
            mapa[y][x] = anterior
            mapa_colores [y][x] = color_anterior
            mapa_fondo [y][x] = fondo_anterior
            
            y, x = movimiento(y, x, accion, alto-2, ancho-2)
            
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
            
            if tipo == "inicio":
                if inicio == 1:
                    while True:
                        opcion = input("Parece que ya tienes un punto de inicio registrado, ¿quieres borrar el anterior y guardar este (S/N)? : ").upper()
                        if opcion == "S":
                            mapa_caracteristicas [punto_inicio[0]][punto_inicio[1]] = ""
                            mapa_caracteristicas [y][x] = "inicio"
                            
                            punto_inicio[0] = y
                            punto_inicio[1] = x
                            break
                        elif opcion == "N":
                            break
                        else:
                            print("Hubo un error camarada, solo se admiten S o N como respuesta, por favor, intentalo nuevamente")
            else:
                mapa_caracteristicas[y][x] = tipo
            
        elif accion == "backspace":
            anterior = "   "
            mapa[y][x] = "   "
            mapa_colores[y][x] = 3
            mapa_fondo[y][x] = 6
            mapa_caracteristicas [y][x] = ""
            
        elif ((accion == "'")|(accion == "¿")):
            comandos()
        
        elif accion == "m":
            material = seleccionar_material(materiales)
        
        elif accion == "n":
            del_usuario.append(nuevo_material())
        
        elif accion == "c":
            color = seleccionar_color()
        
        elif accion == "p":
            personaje = crear_personaje()
            
        elif accion == "q":
            mapa[y][x] = anterior
            y = punto_inicio[0]
            x = punto_inicio[1]
            material = personaje[0]
            color = personaje[1]
            prueba = True
        
        elif accion == "r":
            while True:
                respuesta = input("Quiere crear una nueva expresion para un personaje (S/N)? : ").upper().strip()
                if respuesta == "S":
                    lista = crear_expresion_npc()
                    npcs_caras[lista[1]] = lista[0]
                    break
                elif respuesta == "N":
                    break
                else:
                    print("Solo podemos leer S o N, intente contestar de esa manera")
                    
        elif accion == "t":
            tipo = tipo_material()
            if tipo == "inicio":
                inicio = 1
        
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