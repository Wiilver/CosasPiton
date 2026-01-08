import json
import os

def menu():
    direc = os.getcwd()
    rutas = os.listdir(direc)
    if not rutas.__contains__("Calificaciones.json"):
        calificaciones = {}
        archivo = open("Calificaciones.json", "x")
        archivo.close()
    
        with open("Calificaciones.json", "w") as archivo:
            json.dump(calificaciones, archivo)
        
    while True:
        opc = opciones()
        if opc == 1:
            ver_calif()
                
        elif opc == 2:
            edit_calif()
            
        elif opc == 3:
            agg_sem()
            
        elif opc == 4:
            edit_mat()
            
        elif opc == 5:
            elim_sem()
            
        elif opc == 6:
            elim_mat()
            
        elif opc == 7:
            break

def opciones():
    while True:
        opc = int(input(
            "Por favor, seleccione una de las siguientes opciones:\n"
            "1.- Ver las calificaciones de un semestre\n"
            "2.- Editar las calificaciones de un semestre\n"
            "3.- Agregar un semestre\n"
            "4.- Editar las materias de un semestre\n"
            "5.- Eliminar un semestre\n"
            "6.- Eliminar la materia de un semestre\n"
            "7.- Ordenar semestres"
            "8.- Salir\n"
            "Opcion : "
        ))
        if((opc < 1)|(opc > 8)):
            os.system("cls")
            print("Parece que hubo un problema con lo que escribiste, por favor, intentalo de nuevo\n")
        else:
            return opc

def ver_calif():
    with open("Calificaciones.json", "r") as archivo:
        datos = json.load(archivo)

    if len(datos.keys()) == 0:
        os.system("cls")
        print("Parece que aun no has ingresado ningun semestre, intentelo de nuevo\n")
    else:
        while True:
            print("Esta es una lista de los semestres que tienes creados:\n")
            contador = 0
            for i in datos.keys():
                contador+=1
                print(f"{i}")
            opc = input("\nSeleccione un semestre : ")
            if not datos.keys().__contains__(opc):
                os.system("Parece que ningun semestre coincide con tu respuesta, por favor, intentalo de nuevo\n")
            else:
                for i in range(0, len(datos[opc])):
                    print(f"{datos[opc][i-1]}\n")
                break
        
def edit_calif():
    with open("Calificaciones.json", "r") as archivo:
        datos = json.load(archivo)
    if len(datos.keys()) == 0:
        print("Necesitas tener un semestre creado para hacer esto\n")
    else:
        while True:
            print("Esta es una lista de los semestres que tienes creados:\n")
            contador = 0
            for i in datos.keys():
                contador+=1
                print(f"{i}")
            opc = input("\nSeleccione un semestre : ")
            if not datos.keys().__contains__(opc):
                os.system("Parece que ningun semestre coincide con tu respuesta, por favor, intentalo de nuevo\n")
            else:
                break
        while True:
            nombre = input("Seleccione un nombre para su materia : ")
            
    
def agg_sem():
    with open("Calificaciones.json", "r") as archivo:
        datos = json.load(archivo)
    while True:
        print(datos)
        opc = input("Ingrese el numero del semestre que quiere agregar : ")
        if ((int(opc)<1)|(int(opc)>9)):
            os.system("cls")
            print("Los semestres solo van del 1 al 9, por favor, intentalo de nuevo\n")
        elif datos.keys().__contains__(opc):
            os.system("cls")
            print("Parece que ya hay un semestre con este numero, por favor, intentalo de nuevo\n")
        else:
            os.system("cls")
            datos[opc] = ""
            with open("Calificaciones.json", "w") as archivo:
                json.dump(datos, archivo)
            break
        
def edit_mat():
    print()
def elim_sem():
    print()

def elim_mat():
    print()

menu()