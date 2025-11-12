import random

phjug = 10
phnpc = 10
Stamina = 3

Turno = 0

Seguir = True

def Impresion(vidajug, vidanpc, stamina):
    BarJug = ""
    BarNpc = ""
    BarStamina = ""
    
    rep = int(vidajug/2)
    
    for i in range (0, rep):
        BarJug = BarJug + "▓"
        
    if vidajug % 2 == 1:
        BarJug = BarJug + "▒"
    
    rep = int(vidanpc/2)
    
    for i in range(0, stamina):
        BarStamina = BarStamina + "[] "
    
    for i in range(0,rep):
        BarNpc = BarNpc + "▓"
        
    if vidanpc%2 == 1:
        BarNpc = BarNpc + "▒"
    
    if len(BarNpc)<5:
        for i in range(0, 5-len(BarNpc)):
            BarNpc = BarNpc + " "
    
    if len(BarJug)<5:
        for i in range(0, 5-len(BarJug)):
            BarJug = BarJug + " "
            
    print('╔══════════════════════════════╗ \n'
          '║    HPJUG            HPNPC    ║ \n'
         f'║    {BarJug}            {BarNpc}    ║ Estamina : {BarStamina}\n'
          '║                              ║ \n'
          '║                  |  (%)  |   ║ \n'
          '║                  ■-q███p-■   ║ \n'
          '║     () /            █ █      ║ \n'
          '║     █-/                      ║ \n'
          '║    / \                       ║ \n'
          '╚══════════════════════════════╝')
while Seguir:
    Nosabescribir = True
    Defender = False
    #bORRALO LUEGO
    Turno = 0
    Impresion(phjug,phnpc, Stamina)
    if Turno == 0:
        print("1.- Atacar   2.- Defenderse   3.- Curarse   4.- Huir")

        while Nosabescribir:
            Hizo = input("Introduzca su comando: ")
            if ((Hizo!="1")&(Hizo!="2")&(Hizo!="3")&(Hizo!="4")):
                print("Solo se admite un numero hermnano, aprendamos a escribir")
            else:
                Nosabescribir = False
                
        Hizo = int(Hizo)

        if Hizo == 1:
            if Stamina > 0:
                phnpc -=1
                Stamina -=1
                print(f"Atacaste al enemigo, te quedan {Stamina} de estamina")
            else:
                print("Estas demasiado cansado como para atacar ¡Perdiste tu turno!")
        elif Hizo == 2:
            Defender = True
            Stamina += 1
            print("Te proteges y recupersaste 1 de estamina")
        elif Hizo == 3:
            if phjug<9:
                phjug += 2
                print(f"Te curaste, ahora tienes {phjug} de vida y {Stamina} de estamina")
            elif phjug == 9:
                phjug = 10
                print(f"Te curaste, ahora tienes 10 de vida y {Stamina} de estamina")
            else:
                print("Desperdiciaste tu oportunidad curando un sano")
        else:
            print("Trataste de huir pero la criatura te siguio de todos modos")
        Turno = 1
    else:
        Rnd = 3
        if phnpc < 9:
            Rnd = 1
        
        Rnd = random.randrange(Rnd, 4)
        