import keyboard, time, os, json
from colorama import Fore, Back

#Falta hacer que se pueda editar un escenario despues de haberlo creado, que detecte si ya hay otras pantallas creadas
#Falta hacer que el archivo principal le designes la pantalla de inicio
#Falta que hagas un modo para jugar como tal

#Variables

alto= 0
ancho = 0
y = 0
x = 0

juegos = []

malos_caracteres = ["'", '"', "?", "¿", " ", "|", "/", "\\", "<", ">", "*", ":", ".", ","]

personaje = [" O ", 3]

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


def crear_expresion_npc(npcs_caras):
    os.system("cls")
    input("Crearemos una expresion para mostrar en una conversacion...\n")
    while True:
        nombre_expresion = input("Primero que nada, introduzca el nombre de su expresion : ")
        if not nombre_expresion:
            print("Necesita tener un nombre, por favor intentelo de nuevo\n")
        else:
            break
    cara = hacer_cara()
    cara = cara_npc(material, cara)
    npcs_caras[nombre_expresion] = cara
    
    with open(f"juego_{titulo}.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
        
    datos["caras"] = npcs_caras
    
    with open(f"juego_{titulo}.json", "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, ensure_ascii=False)
    
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
                respuesta = input("Seguro que así quiere que se vea el npc? Esta configuracion no se podra cambiar (S/N) : ").upper().strip()
                if respuesta == "S":
                    return cara
                elif respuesta != "N":
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
                respuesta = int(input("Esta es la lista de colores que puede seleccionar:\n"
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
        if ((respuesta < 0)|(respuesta > 7)):
            print("Hermano, el numero debe de estar entre el 1 y el 8, intentalo nuevamente")
        else:
            break
    input("Presione ENTER para salir...")
    
    return respuesta

def seleccionar_material(materiales):
    input("Presione ENTER para continuar...")
    while True:
        while True:
            try:
                respuesta = int(input("Estas son las categorias de materiales disponibles \n"
                                "1.- Lineas\n"
                                "2.- Texturas \n"
                                "3.- Bloques\n"
                                "4.- Otros\n"
                                "5.- Del usuario\n"
                                "Opcion : "))-1
                break
            except:
                print("Hermano, solo puedes ingresar numeros, por favor intentalo de nuevo")
        if ((respuesta < 0)|(respuesta > 4)):
            print("Hermano, el numero debe de estar entre 1 y 5, por favor intentalo nuevamente")
        else:
            break
    if respuesta == 4:
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
                        respuesta = int(input("Material : "))-1
                        break
                    except:
                        print("Hermano, solo puedes ingresar numeros, por favor intentalo nuevamente")
                if ((respuesta < 0)|(respuesta > len(materiales[4]))):
                    print(f"Hermano, el indice debe de estar entre 1 y {len(materiales[4])}, por favor intentalo nuevamente")
                else:
                    break
            material = materiales[4][respuesta]
            input("Presione ENTER para salir...")
            return material
    elif respuesta == 0:
        while True:
            while True:
                try:
                    respuesta = int(input("Las lineas tienen dos subcategorias:\n"
                                    "1.- Lineas simples\n"
                                    "2.- Lineas dobles\n"
                                    "Favor de seleccionar que opcion desea : "))-1
                    break
                except:
                    print("Hermano, solamente se admiten numeros, por favor intentalo nuevamente")
            if ((respuesta < 0)|(respuesta > 1)):
                print("Hermano, solo se admiten los valores 1 y 2, por favor intentalo nuevamente")
            else:
                break
        contador = 1
        for i in materiales[0][respuesta]:
            print(f"{contador}.- {i}")
            contador +=1
        print()
        while True:
            while True:
                try:
                    respuesta_2 = int(input("Material : "))-1
                    break
                except:
                    print("Hermano, solo se admiten numeros, por favor intentalo nuevamente")
            if ((respuesta_2 < 0)|(respuesta_2 > len(lineas_dobles))):
                print(f"Hermano, el indice debe de estar entre 1 y {len(materiales[0][respuesta])}, por favor intentalo nuevamente")
            else:
                break
        material = materiales[0][respuesta][respuesta_2]
        input("Presione ENTER para salir...")
        return material
    else:
        contador = 1
        for i in materiales[respuesta]:
            print(f"{contador}.- {i}")
            contador += 1
        print()
        while True:
            while True:
                try:
                    respuesta_2 = int(input("Material : "))-1
                    break
                except:
                    print("Hermano, solo se admiten numeros, por favor intentalo nuevamente")
            if ((respuesta_2 < 0)|(respuesta_2 > len(materiales[respuesta]))):
                print(f"Hermano, el indice debe de estar entre 1 y {len(materiales[respuesta])}, por favor, intentalo de nuevo")
            else:
                break
        material = materiales[respuesta][respuesta_2]
        input("Presione ENTER para salir...")
        return material

def hacer_cara():
    lista = []
    lista.clear()
    for i in range (0,7):
        lista.append([])
        for j in range (0,7):
            lista[i].append("   ")
            if ((i == 0)|(i == 6)):
                lista[i][j] = "═══"
            if ((j == 0)|(j == 6)):
                lista[i][j] = " ║ "
    lista[0][0] = " ╔═"
    lista[6][0] = " ╚═"
    lista[0][6] = "═╗ "
    lista[6][6] = "═╝ "
    return lista
    
def hacer_mapa(mapa, mapa_colores, mapa_caracteristicas, mapa_fondo, alto , ancho):
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
    return mapa, mapa_fondo, mapa_colores, mapa_caracteristicas

def impresion_cara(cara):
    for i in cara:
        for j in i:
            print(j, end="")
        print()

def impresion(mapa, mapa_fondo, mapa_colores):
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

def movimiento(y, x, accion, altura, anchura):
    if ((accion == "flecha arriba") | (accion == "w")):
        if y > 1:
            y -= 1
    elif ((accion == "flecha abajo") | (accion == "s")):
        if y < altura:
            y += 1
    elif ((accion == "flecha derecha") | (accion == "d")):
        if x < anchura:
            x += 1
    elif ((accion == "flecha izquierda") | (accion == "a")):
        if x > 1:
            x -= 1
    return y, x

def movimiento_prueba(y, x, altura, anchura, accion, mapa_caracteristicas):
    if ((accion == "flecha arriba") | (accion == "w")):
        if y > 1:
            if mapa_caracteristicas[y-1][x] == "pared":
                print("No puedes moverte en esa direccion, hay algo que te detiene")
                time.sleep(.1)
                keyboard.read_event()
            else:
                y -= 1
    elif ((accion == "flecha abajo") | (accion == "s")):
        if y < altura-2:
            if mapa_caracteristicas[y+1][x] == "pared":
                print("No puedes moverte en esa direccion, hay algo que te detiene")
                time.sleep(.1)
                keyboard.read_event()
            else:
                y += 1
    elif ((accion == "flecha derecha") | (accion == "d")):
        if x < anchura-2:
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

def nueva_conversacion(npcs_caras, textos):
    os.system("cls")
    input("Crearemos una conversacion...\n")
    while True:
        nombre_conversacion = input("Por favor, pongale un nombre a la conversacion : ")
        if not nombre_conversacion:
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
                        
                        escoger_texto = input("Esta es una lista de los textos que has creado, escoge cual quieras usar : ")
                        print()
                        if not textos.keys().__contains__(escoger_texto):
                            print("Respondiste con una clave que no existe, por favor, intentalo de nuevo")
                        elif not escoger_texto:
                            print("Hermanito, por favor, minimo contesta algo")
                        else:
                            conversacion.append([escoger_cara, escoger_texto])
                            while True:
                                respuesta = input("Deseas agregar otra viñeta (S/N) : ").upper().strip()
                                if ((respuesta != "S")&(respuesta != "N")):
                                    print("Hermano, solo se admiten S o N como respuestas, por favor intentalo nuevamente")
                                else:
                                    break
                        if respuesta == "N":
                            return conversacion, nombre_conversacion
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
            nombre_texto = input("Para crear un texto, primero introduce el titulo del mismo : ")
            if not nombre_texto:
                print("Debes de poner por lo mismo un caracter, por favor, intentalo de nuevo")
            else:
                break
    while True:
        texto = input("Ahora introduce el texto : ")
        if not texto:
            print("Necesiitas poner algo dentro, por favor, intentalo de nuevo")
        else:
            contenido.append(texto)
            while True:
                respuesta= input("Quieres agregar otra linea de texto (S/N)? : ").upper()
                if ((respuesta!= "S")&(respuesta != "N")):
                    print("Por favor, solo se admite S o N como respuesta, escriba bien mi estimado")
                else:
                    break
            if respuesta == "N":
                break
    return nombre_texto, contenido

def tipo_material(conversaciones, npcs_caras, textos):
    print("Presione ENTER para continuar")
    while True:
        while True:
            try:
                respuesta = int(input("Seleccione el tipo de material que quiere usar:\n"
                    "1.- Pared\n"
                    "2.- Texto\n"
                    "3.- Npc\n"
                    "4.- Conectar pantalla\n"
                    "5.- Nulo\n"
                    "6.- Punto de inicio\n"
                    "7.- Interaccion\n"
                    "Tipo : "))
                break
            except:
                print("Solo se admiten valores numericos, por favor, intentelo de nuevo")
        if ((respuesta < 1)|(respuesta > 7)):
            print("Los valores deben de ir de 1 a 5, por favor, intentelo de nuevo")
        else:
            break
    
    if respuesta == 1:
        return "pared"
    
    elif ((respuesta == 2)|(respuesta == 7)):
        eligio = respuesta
        if not textos:
            while True:
                respuesta = input("Parece que no tienes textos hechos, quieres crear uno (S/N)?: ").upper().strip()
                if respuesta == "S":
                    nombre_texto, contenido = nuevo_texto()
                    textos[nombre_texto] = contenido
                    
                    with open(f"juego_{titulo}.json", "r", encoding="utf-8") as archivo:
                        datos = json.load(archivo)
                    
                    datos["textos"] = textos
                    
                    with open(f"juego_{titulo}.json", "w", encoding="utf-8") as archivo:
                        json.dump(datos, archivo, ensure_ascii=False)
                        
                    if eligio == 2:
                        return f"texto_{nombre_texto}"
                    else:
                        return f"interaccion_{nombre_texto}"
                    
                elif respuesta == "N":
                    break
                else:
                    print("Favor de utilizar una S o una N como respuesta")
        else:
            while True:
                respuesta = input("Quiere crear un texto nuevo o utilizar uno antiguo (N/A)? : ").upper().strip()
                if respuesta == "N":
                    nombre_texto, contenido = nuevo_texto()
                    textos[nombre_texto] = contenido
                    
                    with open(f"juego_{titulo}.json", "r", encoding="utf-8") as archivo:
                        datos = json.load(archivo)
                    
                    datos["textos"] = textos
                    
                    with open(f"juego_{titulo}.json", "w", encoding="utf-8") as archivo:
                        json.dump(datos, archivo, ensure_ascii=False)
                        
                    if eligio == 2:
                        return f"texto_{nombre_texto}"
                    else:
                        f"interaccion_{nombre_texto}"
                elif respuesta == "A":
                    print("Esta es una lista de los textos que ya tienes hechos:")
                    contador = 1
                    for i in textos.keys():
                        print(f"{contador}.- {i}")
                    respuesta = input("Seleccione el titulo del texto que quiera reutilizar : ")
                    if textos.keys().__contains__(respuesta):
                        if eligio == 2:
                            return f"texto_{respuesta}"
                        else:
                            return f"interaccion_{respuesta}"
                else:
                    print("Por favor, utilizar N o A como respuesta")
    
    elif respuesta == 3:
        print()
        if not npcs_caras:
            while True:
                respuesta = input("Parece que aún no tienes ninguna expresion hecha, deseas crear una (S/N)? : ").upper().strip()
                if respuesta == "S":
                    print("\nPrimero crearas la expresion en si, es como al hacer un mapa, pero el único comando activo es M, ENTER y BACKSPACE")
                    input("Cuando estes contento con como se ve presiona ESC, si entendiste esto, presiona ENTER para continuar...")
                    print()
                    crear_expresion_npc(npcs_caras)
                    
                    with open(f"juego_{titulo}.json", "r", encoding="utf-8") as archivo:
                        datos = json.load(archivo)
                        
                    datos["caras"] = npcs_caras
                    
                    with open(f"juego_{titulo}.json", "w", encoding="utf-8") as archivo:
                        json.dump(datos, archivo, ensure_ascii=False)
                    
                    print()
                    break
                elif respuesta == "N":
                    return ""
                else:
                    print("Solo puedes usar S o N como respuesta, por favor, contesta bien")
        if not textos:
            os.system("cls")
            while True:
                respuesta = input("Para crear un npc necesitas tener minimo un texto creado, deseas hacer uno nuevo (S/N)? : ").upper().strip()
                if respuesta == "S":
                    print()
                    nombre_texto, contenido = nuevo_texto()
                    textos[nombre_texto] = contenido
                    
                    with open(f"juego_{titulo}.json", "r", encoding="utf-8") as archivo:
                        datos = json.load(archivo)
                    
                    datos["textos"] = textos
                    
                    with open(f"juego_{titulo}.json", "w", encoding="utf-8") as archivo:
                        json.dump(datos, archivo, ensure_ascii=False)
                    
                    print()
                    break
                elif respuesta == "N":
                    return ""
                else:
                    print("\nPor favor, esfuercese para contestar con S o N solamente e intentelo de nuevo\n")
        if not conversaciones:
            os.system("cls")
            while True:
                respuesta = input("Para definir un npc es necesario que tengas una conversacion creada, deseas hacer una (S/N)? : ").upper().strip()
                if respuesta == "S":
                    contenido, nombre_conversacion = nueva_conversacion(npcs_caras, textos)
                    conversaciones[nombre_conversacion] = contenido
                    
                    with open(f"juego_{titulo}.json", "r", encoding="utf-8") as archivo:
                        datos = json.load(archivo)
                        
                    datos["conversaciones"] = conversaciones
                        
                    with open(f"juego_{titulo}.json", "w", encoding="utf-8") as archivo:
                        json.dump(datos, archivo, ensure_ascii=False)
                    
                    return f"npc_{nombre_conversacion}"
                elif respuesta == "N":
                    break
                else:
                    print("\nPor favor, esfuercese para contestar con S o N solamente e intentelo de nuevo\n")
        else:
            os.system("cls")
            while True:
                respuesta = input("Parece que ya tiene alguna conversacion, desea usar una antigua o crear una nueva(N/A)? : ").upper().strip()
                if respuesta == "N":
                    contenido, nombre_conversacion = nueva_conversacion(npcs_caras, textos)
                    conversaciones[nombre_conversacion] = contenido

                    with open(f"juego_{titulo}.json", "r", encoding="utf-8") as archivo:
                        datos = json.load(archivo)
                        
                    datos["conversaciones"] = conversaciones
                        
                    with open(f"juego_{titulo}.json", "w", encoding="utf-8") as archivo:
                        json.dump(datos, archivo, ensure_ascii=False)
                    
                    return f"npc_{nombre_conversacion}"
                elif respuesta == "A":
                    while True:
                        os.system("cls")
                        contador = 1
                        for i in conversaciones.keys():
                            print(f"{contador}.- {i}")
                            contador += 1
                        print()
                        nombre_conversacion = input("Esta es una lista de las conversaciones que tienes creadas, escribe el nomrbe de la que quieras usar : ")
                        if conversaciones.keys().__contains__(nombre_conversacion):
                            return f"npc_{nombre_conversacion}"
                        else:
                            print("Parece que lo que introdujiste no concuerda con el nombre de ninguna conversacion, por favor, intentalo nuevamente")
                    
    elif respuesta == 4:
        with open(f"juego_{titulo}.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            
            if not "pantallas":
                print("Hermano, no tienes pantallas creadas de momento")
                return ""
            
            else:
                pantallas = datos["pantallas"].keys()
                while True:
                    os.system("cls")
                    for i in pantallas:
                        print(i, "\n")
                    respuesta = input("Estos son las otras pantallas que tienes creadas, introduce el nombre de la que quieras usar : ")
                    if not respuesta in pantallas:
                        print("La respuesta no coincide con ninguna pantalla, por favor, intentalo nuevamente")
                    else:
                        return f"conector_{respuesta}"

    elif respuesta == 5:
        return ""
    
    elif respuesta == 6:
        return "inicio"
    
def mostrar_conversacion(mapa_caracteristicas, conversaciones, npcs_caras, textos, y, x):
    input(...)
    nombre_conversacion = mapa_caracteristicas[y][x].split("_")[1]
    largo = len(conversaciones[nombre_conversacion])
    for i in range(0, largo):
        print (conversaciones[nombre_conversacion][i][0])
        for j in npcs_caras[conversaciones[nombre_conversacion][i][0]]:
            for k in j:
                print(k, end="")
            print()
        for k in textos[conversaciones[nombre_conversacion][i][1]]:
            input(f"{k}\n") 

def leer(mapa_caracteristicas, y, x, textos):
    nombre_texto = mapa_caracteristicas[y][x].split("_")[1]
    input("...")
    for i in textos[nombre_texto]:
        input(f"{i}\n")

#Empieza la cosa
def crear_pantalla():
    
    
    with open(f"juego_{titulo}.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
    
    personaje = datos["personaje"]
    conversaciones = datos["conversaciones"]
    npcs_caras = datos["caras"]
    textos = datos["textos"]
    pantallas = datos["pantallas"]
    del_usuario = datos["materiales_usuario"]    

    
    alto= 0
    ancho = 0
    y = 0
    x = 0

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

    tipo = ""

    material = " O "
    anterior = "   "

    fondo = 6
    fondo_anterior = 6

    color = 3
    color_anterior = 3

    salir = "N"
    inicio = 0
    prueba = False
    
    #Aqui debo de poner un if, si la cosa ya existia, para hacer un load de las variables  y saltarse lo de hacer mapa y las dimensiones
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

    lista = hacer_mapa(mapa,mapa_colores, mapa_caracteristicas, mapa_fondo, alto, ancho)
    mapa = lista[0]
    mapa_fondo = lista[1]
    mapa_colores = lista[2]
    mapa_caracteristicas = lista[3]
    hacer_cara()

    impresion(mapa, mapa_fondo, mapa_colores)

    while True:
        conversaciones.update()
        textos.update()
        accion = keyboard.read_key().lower()
        
        if prueba:
            if moverse.__contains__(accion):
                mapa[y][x] = anterior
                mapa_colores [y][x] = color_anterior
                mapa_fondo [y][x] = fondo_anterior
                
                y, x = movimiento_prueba(y, x, alto, ancho, accion, mapa_caracteristicas)
                
                anterior = mapa[y][x]
                fondo_anterior = mapa_fondo[y][x]
                color_anterior = mapa_colores[y][x]
                
                mapa[y][x] = material
                mapa_fondo [y][x] = fondo
                mapa_colores [y][x] = color
                
                if mapa_caracteristicas[y][x].startswith("texto"):
                    leer(mapa_caracteristicas, y, x, textos)
                    
                elif mapa_caracteristicas[y][x].startswith("npc"):
                    mostrar_conversacion(mapa_caracteristicas, conversaciones, npcs_caras, textos, y, x)
                    
                elif mapa_caracteristicas[y][x].startswith("interaccion"):
                    print("Tu personaje esta pensando algo, presiona ENTER para escucharlo")
                    time.sleep(.1)
                    pensar = keyboard.read_key()
                    if pensar == "enter":
                        leer(mapa_caracteristicas, y, x, textos)
                
            elif accion == "q":
                prueba = False
                
        else:
            if moverse.__contains__(accion):
                mapa [y][x] = anterior
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
                            respuesta = input("Parece que ya tienes un punto de inicio registrado, ¿quieres borrar el anterior y guardar este (S/N)? : ").upper()
                            if respuesta == "S":
                                mapa_caracteristicas [punto_inicio[0]][punto_inicio[1]] = ""
                                mapa_caracteristicas [y][x] = "inicio"
                                
                                punto_inicio[0] = y
                                punto_inicio[1] = x
                                break
                            elif respuesta == "N":
                                break
                            else:
                                print("Hubo un error camarada, solo se admiten S o N como respuesta, por favor, intentalo nuevamente")
                else:
                    mapa_caracteristicas[y][x] = tipo
                
            elif accion == "backspace":
                fondo_anterior = 6
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
                
                with open(f"juego_{titulo}.json", "r", encoding="utf-8") as archivo:
                    datos = json.load(archivo)
                    
                datos["materiales_usuario"] = del_usuario

                with open(f"juego_{titulo}.json", "w", encoding="utf-8") as archivo:
                    json.dump(datos, archivo, ensure_ascii=False)
            
            elif accion == "c":
                color = seleccionar_color()
            
            elif accion == "p":
                personaje = crear_personaje()
                with open(f"juego_{titulo}.json", "r") as archivo:
                    datos = json.load(archivo)
                
                datos["personaje"] = personaje
                with open(f"juego_{titulo}.json", "w", encoding="utf-8") as archivo:
                    json.dump(datos, archivo, ensure_ascii=False)
                    
            elif accion == "q":
                mapa[y][x] = anterior
                y = punto_inicio[0]
                x = punto_inicio[1]
                material = personaje[0]
                color = personaje[1]
                fondo_anterior = 6
                fondo = 6                
                prueba = True
            
            elif accion == "r":
                while True:
                    respuesta = input("Quiere crear una nueva expresion para un personaje (S/N)? : ").upper().strip()
                    if respuesta == "S":
                        crear_expresion_npc(npcs_caras)
                        break
                    elif respuesta == "N":
                        break
                    else:
                        print("Solo podemos leer S o N, intente contestar de esa manera")
                        
            elif accion == "t":
                tipo = tipo_material(conversaciones, npcs_caras, textos)
                if tipo == "inicio":
                    inicio = 1
            
            elif accion == "f":
                fondo = seleccionar_color()
                
            elif accion == "esc":
                #Aqui deberia de poner un if antes, si ya existe una pantalla, para mas bien actualizar el json
                while True:
                    salir = input("Quieres guardar los cambios que le hiciste a la pantalla? Esto puede ser cambiado posteriormente (S/N) : ").upper().strip()
                    if salir == "S":
                        while True:
                            mal_nombre = False
                            nombre_pantalla = input("Por favor, pongale un nombre a la pantalla : ")
                            if not nombre_pantalla:
                                print("Hermano, por favor llamalo de alguna manera")
                            else:
                                while True:
                                    for i in malos_caracteres:
                                        if i in nombre_pantalla:
                                            mal_nombre = True
                                    if mal_nombre:
                                        print("Parece ser que introdujiste caracteres que no furulan, por favor, intentalo nuevamente")
                                    else:
                                        break
                                break
                        datos = {
                                "alto": alto,
                                "ancho": ancho,
                                "mapa": mapa,
                                "colores": mapa_colores,
                                "fondo": mapa_fondo,
                                "caracteristicas": mapa_caracteristicas
                                }
                        
                        archivo = open(f"mapa_{nombre_pantalla}.json", "x")
                        archivo.close()

                        with open(f"juego_{titulo}.json", "r", encoding="utf-8") as archivo:
                            datos = json.load(archivo)
                        
                        datos["pantallas"].append(nombre_pantalla)
                        
                        with open(f"juego_{titulo}.json", "w", encoding= "utf-8") as archivo:
                            json.dump(datos, archivo, ensure_ascii=False)
                        
                        with open(f"mapa_{nombre_pantalla}.json", "w", encoding="utf-8") as pantalla:
                            json.dump(datos, pantalla, ensure_ascii=False)
                        break
                        
                    elif respuesta == "N":                  
                        break
            
            else:
                print("No se reconocio el comando, presione cualquier tecla para continuar")
                keyboard.read_key()
            
            if salir == "S":
                break
            
        time.sleep(.1)
        os.system("cls")
        
        if not prueba:
            print(f"El material que esta usando tiene tipo {tipo}\n")
            print(f"El tipo de esta casilla es {mapa_caracteristicas[y][x]}")
        
        impresion(mapa, mapa_fondo, mapa_colores)
        print(conversaciones)
        print(npcs_caras)
        print(del_usuario)

    os.system("cls")


#Menu principal
while True:
    #Encuentra donde esta instalado el programa
    ruta = os.getcwd()
    
    #En la misma ruta en la que esta el programa, obtiene el nombre de los otros documentos que hay
    archivos = os.listdir(ruta)
    
    #Checamos que exista un archivo que tenga de nombre "juego_"
    for i in archivos:
        if i.startswith("juego_"):
            juegos.append(i)
    
    if not juegos:
        while True:
            respuesta = input("Parece que no tienes ningún juego de Wil\\e, deseas crear uno (S/N)? : ").upper().strip()
            if respuesta == "S":
                while True:
                    titulo = input("Introduzca el nombre de su juego, hay un monton de caracteres prohibidos, entonces relaja : ")
                    if not titulo:
                        print("Hermano, pero tampoco se trata de que no pongas nada\n")
                    else:
                        mal_nombre = False
                        for i in malos_caracteres:
                            if i in titulo:
                                mal_nombre = True
                        if mal_nombre:
                            print(f"Introdujiste un caracter que no esta permitido '{i}', intentalo nuevamente")
                        else:
                            archivo = open(f"juego_{titulo}.json", "x")
                            archivo.close()
                            
                            datos_iniciales = {
                                                "titulo" : f"{titulo}",
                                                "personaje" : [" O ", 3], 
                                                "textos" : textos,
                                                "caras" : npcs_caras,
                                                "conversaciones" : conversaciones,
                                                "materiales_usuario": [],
                                                "pantallas" : []
                                               }
                            
                            with open(f"juego_{titulo}.json", "w", encoding="utf-8") as archivo:
                                json.dump(datos_iniciales, archivo, ensure_ascii = False)                                
                            
                            crear_pantalla()
                            break
            elif respuesta == "N":
                break
            else:
                print("Hermano, solo te aceptare S o N como respuesta, por favor, intentalo de nuevo")
    else:
        while True:
            respuesta = input("Parece que ya tienes juegos creados, deseas jugar uno antiguo o crear uno nuevo (A/N)? : ").upper().strip()
            if respuesta == "A":
                while True:
                    for i in juegos:
                        print(i.split("_")[1])
                    
                    titulo = input("Esta es una lista de los juegos que ya tienes creados, por favor, introduce el nombre del que quieras jugar : ")
                    if juegos.__contains__(f"juego_{titulo}.json"):
                        #
                        #
                        #Aqui debes de terminar
                        #
                        #
                        print("")
                    else:
                        print("El nombre que introdujiste no concuerda con ningun juego de los de la lista, por favor, intentalo de nuevo")
                        os.system("cls")
            if respuesta == "N":
                while True:
                    mal_nombre = False
                    titulo = input("Por favor introduzca un nombre para el juego : ").strip()
                    if not titulo:
                        print("Hermano, pero ponle algo macho")
                    else:
                        for i in malos_caracteres:
                            if i in titulo:
                                mal_nombre = True
                        if mal_nombre:
                            print("Hermano tienes caracteres no permitidos en el nombre, por favor, intentalo de nuevo")
                        else:
                            archivo = open(f"juego_{titulo}.json", "x")
                            archivo.close()
                            
                            datos_iniciales = {
                                                "titulo" : f"{titulo}",
                                                "personaje" : [" O ", 3], 
                                                "textos" : textos,
                                                "caras" : npcs_caras,
                                                "conversaciones" : conversaciones,
                                                "materiales_usuario" : [],
                                                "pantallas" : [] 
                                               }
                            
                            with open(f"juego_{titulo}.json", "w", encoding="utf-8") as archivo:
                                json.dump(datos_iniciales, archivo, ensure_ascii = False)                                
                            
                            input("Ahora, empezaremos a crear las pantallas del juego, presiona ENTER para continuar...")
                            crear_pantalla()
                            while True:
                                respuesta = input("Desea agregar una nueva pantalla (S/N)? : ").upper().strip()
                                if respuesta == "S":
                                    crear_pantalla()
                                elif respuesta == "N":
                                    break
                                else:
                                    print("Hermano, solo se toman S o N como respuestas validas, por favor, intentalo de nuevo")