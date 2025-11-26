import re
import os
import json
import numpy 
import statistics
import matplotlib.pyplot as plt

#from pia import datos   
#os.chdir(r"C:\PB_pia\CosasPiton\Pia")
#os.chdir("/home/luis/mangoProyecto/CosasPiton/Pia")
def graficar():
    try:
        jasones = []
        ruta = os.chdir("E:\\Vs Code Programas\\Jueguito\\CosasPiton")
        documentos = os.listdir(ruta)
        for i in documentos:
            if i.endswith(".json"):
                jasones.append(i)
        
        while True:
            for i in jasones:
                print(i)
            cosa = input("Escoja uno de los documentos : ")
            if cosa in jasones:
                break
        
        with open(f"{cosa}", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

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
                año = re.findall("d{4}$", i["birth_date"])
                nacimientos.append(año)

            if "death_date" in i.keys():
                año = re.findall("d{4}$", i["death_date"])
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

        if num_reseñas > 0:
            porcentaje_reseñas.append(int((reseñas[0]/num_reseñas)*100))
            porcentaje_reseñas.append(int((reseñas[1]/num_reseñas)*100))
            porcentaje_reseñas.append(int((reseñas[2]/num_reseñas)*100))
            porcentaje_reseñas.append(int((reseñas[3]/num_reseñas)*100))
            porcentaje_reseñas.append(int((reseñas[4]/num_reseñas)*100))
        else:
            porcentaje_reseñas = [0]
        porcentaje_reseñas_labels = [1,2,3,4,5]

        moda_reseñas = statistics.mode(ratings)
        desviacion_estandar = int(statistics.stdev(reseñas))

        reseñas_media = numpy.mean(reseñas)
        nacimiento_media = numpy.mean(nacimientos)
        muertes_media = numpy.mean(decesos)
        trabajos_media = numpy.mean(num_trabajos)

        plt.pie(porcentaje_reseñas, labels= porcentaje_reseñas_labels,center=(.175,0))
        plt.title("Reseñas medias para autors buscados",y=1.05)
        plt.text(-2,1.2,f"Media de las reseñas : {reseñas_media}")
        plt.text(-2,1.075,f"Moda de las reseñas : {moda_reseñas}")
        plt.text(-2,-1.2,f"Desviacion estandar de las reseñas : {desviacion_estandar}")
        plt.text(-2,-1.375,f"Numero de trabajos : {num_trabajos[0]}")
        plt.show()
    except Exception as e:
        print("Hubo un error inesperado : ",e)