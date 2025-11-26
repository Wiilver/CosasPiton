estudiantes = []

#nombre, matricula, carrera, calificaciones
#calificaciones = lista, nombre de cada materia, calificacion, fecha y semestre

while True:
    opcion = input("Desea agregar un nuevo estudiante? (S/N) : ").upper()
    if opcion == "N":
        break
    elif opcion == "S":
        calificaciones = []
        try:
            while True:
                nombre = input("Por favor, introduzca el nombre del estudiante : ").strip()
                if not nombre:
                    print("Esta pñs")
                else:
                    print("Nombre de mnierda")
                    break
            while True:
                matricula = int(input("Por favor, introduzca su matricula : "))
                if not matricula:
                    print("Esta regular su pendejada")
                elif matricula < 0:
                    print("Eres del diablo o que pedo")
                else:
                    break
            while True:
                carrera = input("Introduzca su carrera por favor : ").upper()
                if not carrera:
                    print("Como el diego")
                elif carrera.isnumeric():
                    print("Robocop o qpdo")
                else:
                    break
            while True:
                seguir = input("Desea ingresar una materia? (S/N) : ").upper().strip()
                if not seguir:
                    print("Pero pongame algo hermano")
                elif seguir == "N":
                    break
                else:
                    while True:
                        nombre_materia = input("Ingrese el nombre de la materia : ")
                        if not nombre_materia:
                            print("Otro pedo lo del tab")
                        else:
                            break
                    while True:
                        calif = int(input("Introduzca su calificacion obtenida : "))
                        if calif < 0 | calif >100:
                            print("O un genio o un diego")
                        else:
                            break
                    while True:
                        sem = input("Introduzca el semestre en el que la curso (AD/EJ) : ").upper()
                        if ((sem != "AD") & (sem != "EJ")):
                            print("Te lo scaste de los huevos")
                        else:
                            break
                    calificaciones.append({"materia" : nombre_materia, "calificacion" : calif, "semestre" : sem})
            
            estudiantes.append({"estudiante" : nombre, "matricula": matricula, "carrera" : carrera, "calificaciones" : calificaciones})
                        
        except:
           print("Salio mal tu desmadre")

#estudiantes[{nombre:jose}, {nombre:alberto}, {nombre:paite}]
for i in estudiantes:
    #                                    estudiantes[i]["estudiante"]
    print(f"El nombre del estudiante es {i["estudiante"]}, con matricula {i["matricula"]} y de carrera {i["carrera"]} tiene las siguientes califiaciones")
    
    #for j in range(0, len(estudiantes[i]["calificaciones"]))
    for j in i["calificaciones"]:
        #                   estudiantes[i]["calificaciones"][j]["materia"]
        print(f"Materia : {j["materia"]}\nCalificacion : {j["calificacion"]}\nSemestre : {j["semestre"]}\n")
        
for i in range(0, len(estudiantes)):
    print(estudiantes[i])