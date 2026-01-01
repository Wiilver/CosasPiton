import time
import keyboard
import os

paramo = []
velx = vely = 0
x = y = 5
w = a = s = d = False

for i in range(0,20):
    paramo.append([])
    for j in range(0,40):
        paramo[i].append("  ")

def impresion(mapa):
    for i in mapa:
        for j in i:
            print(j, end="")
        print()

while(True):
    time.sleep(.1)
    os.system("cls")
    
    paramo[int(y)][int(x)] = "  "
    

    if ((keyboard.is_pressed("w"))|(keyboard.is_pressed("up"))):
        vely-=.2
        w = True
    else:
        w = False
    if ((keyboard.is_pressed("a"))|(keyboard.is_pressed("left"))):
        velx-=.2
        a = True
    else:
        a = False
    if ((keyboard.is_pressed("s"))|(keyboard.is_pressed("down"))):
        vely+=.2
        s = True
    else:
        s = False
    if ((keyboard.is_pressed("d"))|(keyboard.is_pressed("right"))):
        velx+=.2
        d = True
    else:
        d = False

    x += velx
    y += vely
    
    if ((not w)&(not s)&(vely!=0)):
        if(vely>0):
            vely-=.1
        else:
            vely+=.1
    if ((not a)&(not d)&(velx!=0)):
        if (velx>0):
            velx-=.1
        else:
            velx+=.1
    paramo[int(y)][int(x)] = "XX"
    impresion(paramo)
    