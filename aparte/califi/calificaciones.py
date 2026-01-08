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
            json.dump(calificaciones, archivo, indent=4)
        
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
            "7.- Salir\n"
            "Opcion : "
        ))
        if((opc < 1)|(opc > 7)):
            os.system("cls")
            print("Parece que hubo un problema con lo que escribiste, por favor, intentalo de nuevo\n")
        else:
            return opc

def ver_calif():
    os.system("cls")
    
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
    os.system("cls")
    
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
        with open("Calificaciones.json", "r") as archivo:
            calif = json.load(archivo)
        notas = calif[opc]
        while True:
            while True:
                nombre = input("Seleccione un nombre para su materia : ")
                if not nombre:
                    os.system("cls")
                    print("Parece que no introdujiste nada, por favor, intentalo de nuevo")
                else:
                    break
            while True:
                try:
                    nota = int(input("Ingrese la calificacion que saco en esa materia : "))
                    if not nota:
                        os.system("cls")
                        print("Parece que no introdujiste nada, por favor, intentalo de nuevo")
                    else:
                        break
                except:
                    os.system("cls")
                    print("Parece que introdujiste una palabra, por favor, intentalo de nuevo")
            notas.append({nombre:nota})
            while True:
                cont = input("Desea agregar otra materia (S/N) ? : ").upper()
                if((cont == "S")|(cont == "N")):
                    break
                else:
                    os.system("cls")
                    print("Parece que hubo un error con tu respuesta, por favor, intentalo de nuevo")
            if cont == "N":
                break
            else:
                os.system("cls")
        calif[opc] = notas
        with open("Calificaciones.json", "w") as archivo:
            json.dump(calif, archivo, indent=4)

def agg_sem():
    os.system("cls")
    
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
            datos[opc] = []
            with open("Calificaciones.json", "w") as archivo:
                json.dump(datos, archivo, indent=4)
            break
        
def edit_mat():
    os.system("cls")
    
    with open("Calificaciones.json", "r") as archivo:
        datos = json.load(archivo)
    
    if len(datos) == 0:
        print("Para hacer esto necesitas tener un semestre con calificaciones creado, por favor, intentalo de nuevo\n")
    else:
        while True:
            for i in datos.keys():
                print(i)
            try:
                sem = input("\nPor favor, seleccione el semestre del que necesite editar una materia: ")
                if sem in datos.keys():
                    break
                else:
                    os.system("cls")
                    print("El semestre que introdujiste no estaba entre las opciones, por favor, intentalo de nuevo\n")
            except:
                os.system("cls")
                print("Parece que hubo un error con el dato que introdujiste, por favor, intentalo de nuevo\n")
        if len(datos[sem]) == 0:
            os.system("cls")
            print("Parece que no tiene materias agregadas en este semestre, por favor, intentelo de nuevo\n")
        else:
            while True:
                contador = 1
                for i in datos[sem]:
                    print(f"{contador}.- {i}")
                    contador+=1
                try:
                    mat = int(input("\nSeleccione el numero de la materia que quiera editar : "))
                    if ((mat<1)|(mat>len(datos[sem]))):
                        os.system("cls")
                        print("Seleccionaste una materia fuera de rango, por favor, intentalo de nuevo\n")
                    else:
                        break
                except:
                    os.system("cls")
                    print("Parece que hubo un error con el dato que introdujiste, por favor, intentalo de nuevo\n")
            while True:
                nombre = input(f"\nPor favor, seleccione el nuevo nombre que quiera para la materia (anteriormente era {list(datos[sem][mat-1].keys())[0]}) : ")
                if not nombre:
                    os.system("cls")
                    print("No puedes dejar el nombre vacio, por favor, intentalo nuevamente\n")
                else:
                    try:
                        calif = int(input("Por favor, ingrese la calificacion que saco para esta materia : "))
                        if not calif:
                            os.system("cls")
                            print("No puede dejar este espacio vacio, por favor, intentelo nuevamente\n")
                        else:
                            break
                    except:
                        os.system("cls")
                        print("Parece que hubo un error con el dato que introdujiste, por favor, intentalo nuevamente\n")
            datos[sem][mat-1] = {nombre : calif}
            with open("Calificaciones.json", "w") as archivo:
                json.dump(datos, archivo, indent=4)

def elim_sem():
    with open("Calificaciones.json", "r") as archivo:
        datos = json.load(archivo)
    if len(datos.keys()) == 0:
        os.system("cls")
        print("Para poder eliminar un semestre necesita tener uno creado")
    else:
        while True:
            for i in list(datos.keys()):
                print(f"Semestre {i}")
            try:
                sem = input("\nPor favor, seleccione que semestre quiere borrar, si no quiere borrar ninguno ingrese '0' : ")
                if int(sem)==0:
                    break
                elif sem in datos.keys():
                    datos.pop(sem)
                    with open("Calificaciones.json", "w") as archivo:
                        json.dump(datos, archivo, indent=4)
                    break
            except:
                os.system("cls")
                print("Parece que hubo un error con el dato que introdujiste, por favor, intentalo de nuevo\n")

def elim_mat():
    with open("Calificaciones.json", "r") as archivo:
        datos = json.load(archivo)
    if len(datos.keys()) == 0:
        os.system("cls")
        print("Necesitas tener creado un semestre con materias para poder eliminarle las materias")
    else:
        while True:
            for i in list(datos.keys()):
                print(f"Semestre {i}")
            sem = input("\nPor favor, seleccione el semestre del que quiera eliminar una materia, si quiere cancelar la accion introduzca '0' : ")
            if ((sem in list(datos.keys()))|(sem=="0")):
                break
            else:
                os.system("cls")
                print("El semestre que introdujo no se encuentra entre las opciones, por favor, intentelo de nuevo\n")
        if sem != "0":
            while True:
                contador = 1
                for i in datos[sem]:
                    print(f"{contador}.- {i}")
                try:
                    mat = int(input("Ingrese el numero de la materia que quiere eliminar, si quiere cancelar esta accion ingrese '0' : "))
                    if ((mat>-1)|(mat<=len(datos[sem]))):
                        break
                    else:
                        os.system("cls")
                        print("El indice que diste como respuesta esta fuera del rango admitido, por favor intentalo de nuevo\n")    
                except:
                    os.system("cls")
                    print("Parece que hubo un error con la respesta que diste, por favor intentalo de nuevo\n")
            if mat!=0:
                datos[sem].pop(mat-1)
                with open("Calificaciones.json", "w") as archivo:
                    json.dump(datos, archivo, indent=4)

menu()