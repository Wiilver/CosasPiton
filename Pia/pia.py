import os
import json
import requests
import importlib
def saludo_inicial():
    print("--------------------------------\n",
          "      Bienvenido a Librazos     \n",
          "--------------------------------\n",
          "Este programa esta diseñado para\n",
          "proporcionar informacion concisa\n",
          " resumida y graficada acerca de \n",
          "         LIBROS Y AUTORES       \n",
          "\n",
          "   PRESIONE ENTER PARA INICIAR  \n")
    input()
    
def menu_y_modo():
    #Este comando limpia la consola, para evitar que se sature de texto
    os.system("cls")
    while True:
        modo = 0
        try:
            print(
                "Librazos te da la opcion de buscar autores y libros, por favor, seleccione la opcion que desee :\n",
                "\n1.- Buscar un autor\n",
                "\n2.- Buscar un libro\n",
                )
            modo = int(input("Opcion : "))            
            if ((modo != 1)&(modo !=2)):
                print("El numero que introdujiste se encuentra fuera del rango, por favor, intentalo nuevamente")
                os.system("cls")
                
            else:
                return modo
        except:
            print("Hubo un error en el tipo de dato, por favor, intentalo de nuevo")
        os.system("cls")

def que_buscar(modo):
    os.system("cls")
    if modo == 1:
        print("Esta tratando de buscar un autor\n")
    else:
        print("Esta tratando de buscar un libro")
    while True:
        busqueda = input("Introduzca el nombre de lo que quiera buscar : ")
        if not busqueda:
            os.system("cls")
            print("Necesita introducir al menos un caracter, intentelo de nuevo")
        else:
            busqueda = busqueda.strip().lower()
            NOMBRE = busqueda
            busqueda = busqueda.split(" ")
            cadena = ""
            for i in busqueda:
                cadena = cadena + i + "+"
            return cadena, NOMBRE

def buscar(modo, busqueda):
    if modo == 1:
        url = "https://openlibrary.org/search/authors.json?q=" + busqueda
    else:
        url = "https://openlibrary.org/search.json?q=" + busqueda
    try:
        llamada = requests.get(url)
        llamada.raise_for_status()
        
        datos = llamada.json()
        
        del datos["numFoundExact"]

        if "start" in datos.keys():
            del datos["start"]
        if "documentation_url" in datos.keys():
            del datos["documentation_url"]
        if "q" in datos.keys():
            del datos["q"]
        if "offset" in datos.keys():
            del datos["offset"]
        if "num_found" in datos.keys():
            del datos["num_found"]
        
        if modo == 1:
            for i in datos["docs"]:
                if "_version_" in i.keys():
                    del i["_version_"]
                if "alternate_names" in i.keys():
                    del i["alternate_names"]
                if "author_key" in i.keys():
                    del i["author_key"]
                if "key" in i.keys():
                    del i["key"]
                if "type" in i.keys():
                    del i["type"]
                if "ratings_sortable" in i.keys():
                    del i["ratings_sortable"]
                if "readinglog_count" in i.keys():
                    del i["readinglog_count"]
            return datos
        else:
            for i in datos["docs"]:
                if "author_key" in i.keys():
                    del i["author_key"]
                if "cover_edition_key" in i.keys():
                    del i["cover_edition_key"]
                if "cover_i" in i.keys():
                    del i["cover_i"]
                if "ebook_access" in i.keys():
                    del i["ebook_access"]
                if "has_fulltext" in i.keys():
                    del i["has_fulltext"]
                if "key" in i.keys():
                    del i["key"]
                if "public_scan_b" in i.keys():
                    del i["public_scan_b"]
                if "ia" in i.keys():
                    del i["ia"]
                if "ia_collection_s" in i.keys():
                    del i["ia_collection_s"]
                if "lending_edition_s" in i.keys():
                    del i["lending_edition_s"]
                if "lending_identifier_s" in i.keys():
                    del i["lending_identifier_s"]
                if "id_standard_ebooks" in i.keys():
                    del i["id_standard_ebooks"]
                if "id_wikisource" in i.keys():
                    del i["id_wikisource"]
                if "id_project_gutenberg" in i.keys():
                    del i["id_project_gutenberg"]
        return datos
    except Exception as e:
        print("Hubo un error al tratar de conectarse a la pagina: ", e)

def impresion_y_seleccion(datos, modo):
    #Resulto ser que hay un problema con el API, solo devuelve los primeros 100 resultados que encuentra unu 
    
    os.system("cls")
    if len(datos["docs"]) == 0:
        while True:
            repetir = input("Parece que no hubo ninguna coincidencia con tu busqueda, quieres realizar una nueva (S/N)? : ")
            if repetir == "S":
                opcion = -1
                return opcion
            elif repetir == "N":
                opcion = 0
                return opcion
            else:
                print("Parece que introdujiste una mala respuesta, por favor, intentalo nuevamente")
    elif len(datos["docs"]) <= 10:
        while True:
            os.system("cls")
            print("Esta es una lista de los resultados que coinciden con tu busqueda :\n")
            if modo == 1:
                for i in range(0,datos["numFound"]):
                    print(f"{i+1}.- {datos["docs"][i]["name"]}")
            else:
                for i in range(0,datos["numFound"]):
                    print(f"{i+1}.- {datos["docs"][i]["title"]}")
            try:
                opcion = int(input("\nIngrese el indice que quiera seleccionar : "))
                if ((opcion < 0)|(opcion > datos["numFound"])):
                    print("El numero que introdijiste se encuentra fuera del rango esperado, por favor, intentalo nuevamente")
                else:
                    return opcion
            except:
                input("Hubo un error con el numero que ingresaste, por favor, intentalo nuevamente")
    else:
        pestaña = 1
        while True:
            os.system("cls")
            print(datos["numFound"])
            print(len(datos["docs"]))
            print(f"Pestaña {pestaña} de {len(datos["docs"])//10}\n",
                  "Esta es una lista de los resultados que coinciden con tu busqueda : \n")
            if modo == 1:
                for i in range((pestaña-1)*10,pestaña*10):
                    print(f"{i+1}.- {datos["docs"][i]["name"]}")
            else:
                for i in range((pestaña-1)*10,pestaña*10):
                    print(f"{i+1}.- {datos["docs"][i]["title"]}")
            try:
                print("Puede cambiar de pestaña escribiendo 'der' o 'izq")
                opcion = input("\nIngrese el indice que quiera seleccionar : ").lower().strip()
                if opcion == "der":
                    if pestaña < len(datos["docs"])//10:
                        pestaña +=1
                    else:
                        print("No quedan mas pestañas")
                elif opcion == "izq":
                    if pestaña > 1:
                        pestaña -= 1
                    else:
                        print("No quedan menos pestañas")
                else:
                    opcion = int(opcion)
                    if ((opcion < 1)|(opcion > len(datos["docs"]))):
                        print("El numero que introdijiste se encuentra fuera del rango esperado, por favor, intentalo nuevamente")
                    else:
                        return opcion
            except:
                input("Hubo un error con el numero que ingresaste, por favor, intentalo nuevamente")
            
def menu_busqueda():
    saludo_inicial()
    while True:
        os.system("cls")
        modo = menu_y_modo()
        lista = que_buscar(modo)
        nombre = lista[1]
        datos = buscar(modo, lista[0])
        
        archivo = open(f"{nombre}.json", "x")
        archivo.close()

        #En esta parte del codigo usamos la palabra clave with para no tener la necesidad de cerrar el archivo
        #El encoding es encoding y el ensure ascii es para evitar que truene si usamos caracteres especiales
        #El indent es para que no quede todo en una sola linea
        #En los archivos dejamos creados un archivo para un autor en especifico y un libro en especifico          
        
        with open(f"{nombre}.json", "w", encoding= "utf=8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
        
        opcion = impresion_y_seleccion(datos, modo)
        if opcion == 0:
            break
        elif opcion == -1:
            print("Iniciaremos el proceso nuevamente")
        else:
            #Es el indice del diccionario que tenemos en datos
            return opcion-1, modo, datos

#No sirve
def limpieza_de_datos(nombre):
    with open(f"{nombre}.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
    

def menu_graficas(indice, modo):
    while True:
        os.system("cls")
        print(
            "Esta es una lista de lo que puede hacer con los datos obtenidos:\n"
            "1.- Imprimir los datos de la busqueda que hizo\n"
            "2.- Visualizar graficamente estadisticas de resultados similares\n"
            "3.- Hacer una busqueda distinta\n"
            "4.- Salir\n"
            "Opcion : "
            )
        try:
            opcion = int(input())
            if ((opcion>0)&(opcion<5)):
                break
            else:
                print("La respuesta que introdujiste estuvo fuera del rango esperado")
        except:
            print("Parece que hubo un error con el dato que introdujiste, por favor, intentalo nuevamente")
    if opcion == 1:
        os.system("cls")
        print("Datos de la búsqueda seleccionada:\n")

        try:
            seleccionado = datos["docs"][opcion]
        except Exception as e:
            print("Error al acceder al diccionario seleccionado:", e)
            input("ENTER para continuar")
        
        for llave, valor in seleccionado.items():
            print(f"{llave}: {valor}")

        print("\n----------------------------------")
        input("Presiona ENTER para volver al menú...")
        return menu_graficas(indice, modo)
    elif opcion == 2:
        print("Mostrando gráficas")
        import pia2
        importlib.reload(pia2)         
        input("\nPresiona ENTER para continuar")
        return menu_graficas(indice, modo)
    elif opcion == 3:
        return menu_y_modo()
    lista = menu_busqueda()

    opcion = lista[0]
    modo = lista[1]
    datos = lista[2]
    menu_graficas(modo, opcion , datos["docs"])