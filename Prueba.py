from colorama import Fore, Style, Back

diccionario = {"Hola" : "Hola muy buenas tardes, me complace mucho decirle que me cae muy bien", "Adios" : "Me despido de ti, que tengas suerte"}

lista_llaves = list(diccionario.keys())

for i in lista_llaves:
    print(i)

print(diccionario[lista_llaves[0]])

diccionario["Platica"] = "Parece que el dia esta lindo hoy no?"

print(diccionario["Platica"])

a = "a_b"
a = a.split("_")
print(a)

diccionario.update("Saludo", "Buenas tardes")

print(diccionario[])