import os
import requests
import matplotlib.pyplot as plt

def saludo_inicial():
    input("--------------------------------\n",
          "      Bienvenido a Librazos     \n",
          "--------------------------------\n",
          "Este programa esta diseñado para\n",
          "proporcionar informacion concisa\n",
          " resumida y graficada acerca de \n",
          "         LIBROS Y AUTORES       \n",
          "\n",
          "   PRESIONE ENTER PARA INICIAR  \n")

def menu_y_modo():
    #Este comando limpia la consola, para evitar que se sature de texto
    os.system("cls")
    while True:
        try:
            modo = int(input(
                "Librazos te da la opcion de buscar autores y libros, por favor, seleccione la opcion que desee :\n",
                "\n1.- Buscar un autor\n",
                "\n2.- Buscar un libro\n",
                "\nOpcion : "
                ))
            if ((modo != 1)&(modo !=2)):
                os.system("cls")
                print("El numero que introdujiste se encuentra fuera del rango, por favor, intentalo nuevamente")
            else:
                return modo
        except:
            os.system("cls")
            print("Hubo un error en el tipo de dato, por favor, intentalo de nuevo")

def que_buscar():
    while True:
        busqueda = input("Introduzca el nombre de lo que quiera buscar : ")
        if not busqueda:
            os.system("cls")
            print("Necesita introducir al menos un caracter, intentelo de nuevo")
        else:
            busqueda = busqueda.strip()
            busqueda = busqueda.split(" ")
            cadena = ""
            for i in range(0, len(busqueda)):
                cadena = cadena + i + "+"
            return cadena

def buscar(modo, busqueda):
    if modo == 1:
        url = "https://openlibrary.org/search/authors.json?q=" + busqueda
    else:
        url = "https://openlibrary.org/search.json?q="
    try:
        llamada = requests.get(url)
        llamada.raise_for_status()
        
        datos = llamada.json()
        
        return datos
    except:
        print("Hubo un error al tratar de conectarse a la pagina")
    
def extraccion_autor():
    

def menu():
    saludo_inicial()
    modo = menu_y_modo()
    busqueda = que_buscar()
    datos = buscar(modo, busqueda)
    


#Aqui esta doble para recordar como podia usarse la distincion entre busqueda general y autor
url = "https://openlibrary.org/search/authors.json?q=miguel+de+cervantes+saavedra"
url = "https://openlibrary.org/search.json?q=apuntes+del+subsuelo"

try:
    #Aqui tratamos de llamar a la API
    respuesta = requests.get(url)
    
    #Verificamos si hubo un error con la solicitud
    respuesta.raise_for_status()
    
    #Convertimos los datos a JSON
    datos = respuesta.json()
    
    #Imprimimos los datos
    #El JSON divide la informacion en secciones
    for i in datos["docs"]:
        print(i)
    print()
    """print("Esto sabemos del autor Dostoievski : ", datos)"""
    
    #Ofrecerle al usuario buscar autores o libros
    #Ocuapamos incluir en el algoritmo que busque en cada una de las listas principales y que se vaya con la que tenga el mayor work_count
    #En la parte de los autores hariamos graficos con los distintos numeros de trabajos publicados por idioma
    #En la parte de los libros mostrar la lista completa de libros para que el usuario pueda escoger especificamente que libro usar
    #Usar graficos para ver que años publicaban distintas ediciones
    
except requests.exceptions.RequestException as e:
    print("Salio algo mal hermano : ", e)