informacion = { "nombre": "wilver", "edad":19, "vivo" : True }
if informacion ["vivo"] == True:
    print(informacion)
else:
    print("revivelo")

class Hacer_diccionario():
    def __init__(self,nombre,edad,vivo):
        nombre = self.nombre
        edad = self.edad
        vivo = self.vivo

    def Hacer_pndejada():
        nombre = input("Introduzca su nombre : ")
        edad = input("Intoduzca su edad : ")
        vivo = input("Esta vivo : ")
        datos = {"nombre":nombre,"edad":edad,"vivo":vivo}
        return datos

class Nueva_cosa(Hacer_diccionario):
    def __init__(self,nombre,edad,vivo,pendejo):
        super().__init__(nombre,edad,vivo)
        pendejo = self.pendejo
    def pendejada():
        print("Eres un pendejo")

#dicci = Hacer_diccionario.Hacer_pndejada()


Nueva_cosa.pendejada()
Nueva_cosa.Hacer_pndejada()