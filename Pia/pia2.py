import re
import os
import numpy
import statistics

ruta = os.getcwd()
os.system(f'cd "{ruta}"')
archivos = os.listdir(ruta)
print(archivos)

if "datos.json" not in archivos:
    print("Parece ser que no tienes el archivo necesario para correr este script")
else:
    with open("datos.json", "r", encoding="utf-8") as archivo:
        datos = archivo.read()

temas_principales = []
num_trabajos = []
nacimientos = []
decesos = []
ratings = [0, 0, 0, 0, 0, 0]
for i in datos["docs"]:
    if "top_subjects" in i.keys():
        if len(i["top_subjects"]) <= 3:
            for j in i["top_subjects"]:
                temas_principales.append(j)
        else:
            for j in range(0, 3):
                temas_principales.append(i["top_subjects"][j])
    
    #Estamos usando expresiones regulares para obtener unicamente el año
    if "birth_date" in i.keys():
        año = re.findall("\d{4}", i["birth_date"])
        nacimientos.append(año)
    
    if "death_date" in i.keys():
        año = re.findall("\d{4}", i["death_date"])
        decesos.append(año)
    
    #Esta primera es el numero total
    ratings[0] += i["ratings_count"]
    ratings[1] += i["ratings_count_1"]
    ratings[2] += i["ratings_count_2"]
    ratings[3] += i["ratings_count_3"]
    ratings[4] += i["ratings_count_4"]
    ratings[5] += i["ratings_count_5"]
    
    num_trabajos.append(i["work_count"])

reseñas = []
porcentaje_reseñas = []
num_reseñas = ratings[0]

#Aqui hacemos una nueva lista para guardar las reseñas unicamente, sin guardar los ratings totales
reseñas.append(ratings[1])
reseñas.append(ratings[2])
reseñas.append(ratings[3])
reseñas.append(ratings[4])
reseñas.append(ratings[5])

porcentaje_reseñas.append(reseñas[0]/num_reseñas)
porcentaje_reseñas.append(reseñas[1]/num_reseñas)
porcentaje_reseñas.append(reseñas[2]/num_reseñas)
porcentaje_reseñas.append(reseñas[3]/num_reseñas)
porcentaje_reseñas.append(reseñas[4]/num_reseñas)

moda_reseñas = statistics.mode(ratings)
desviacion_estandar = statistics.stdev(reseñas)

reseñas_media = numpy.mean(reseñas)
nacimiento_media = numpy.mean(nacimientos)
muertes_media = numpy.mean(decesos)
trabajos_media = numpy.mean(num_trabajos)