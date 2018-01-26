import random

print("Bienvenido a la version 2 del selector de juegos")

#definimos los juegos

def piedra ():
    print("Has elegido jugar a Piedra, Papel, Tijeras, Lagarto, Spock")
    intento = int(input("cuantos intentos quieres: "))
    maximo = int(intento/2+1)
    contpc = 0
    contuser = 0
    opciones = ["Piedra","Papel","Tijeras","Lagarto","Spock"]

    while intento > 0:
        def victoria ():
            print("¡Victoria!")
            #contuser += 1            
            ### No entiendo por que en las def no puedo añadir el sumatorio al contador
            
        def derrota ():
            print("¡Derrota!")
            #contpc += 1
            
        usuario = input("Elige: ")
        aleatorio = random.randint(0,4)
        pc = opciones[aleatorio]
        print(usuario,"contra",pc)
        if usuario == pc:
            print("¡Empate!")
        elif usuario == "Piedra":
            if pc == "Tijeras" or pc == "Lagarto":
                victoria()
                contuser += 1
            else:
                derrota()
                contpc += 1
        elif usuario == "Papel":
            if pc == "Piedra" or pc == "Spock":
                victoria()
                contuser += 1
            else:
                derrota()
                contpc += 1
        elif usuario == "Tijeras":
            if pc == "Papel" or pc == "Lagarto":
                victoria()
                contuser += 1
            else:
                derrota()
                contpc += 1
        elif usuario == "Lagarto":
            if pc == "Spock" or pc == "Papel":
                victoria()
                contuser += 1
            else:
                derrota()
                contpc += 1
        elif usuario == "Spock":
            if pc == "Tijeras" or pc == "Piedra":
                victoria()
                contuser += 1
            else:
                derrota()
                contpc += 1
        print("Usuario:",contuser,"PC:",contpc)
        if contuser == maximo:
            print("Tu victoria es tan imponente que no es necesario seguir")
            intento = 0
        elif contpc == maximo:
            print("El azar y el juego han acabado contigo")
            intento = 0
        intento -= 1
        if intento > 1:
            print("Quedan",intento,"intentos")
        elif intento == 1:
            print("Queda",intento,"intento")
    print("Fin del juego")
def adivina ():
    print("Adivina el número del 1 al 100 en 5 intentos")
    numero = random.randint(1,100)
    seguir = True
    intento = 5
    while seguir:
        solucion = int(input("¿Que número es?"))
        if numero == solucion:
            print("Has ganado!")
            seguir = False
        elif numero > solucion:
            print("Es mayor")
        elif numero < solucion:
            print("Es menor")
        intento -= 1
        if intento > 1:
            print("Quedan",intento,"intentos")
        elif intento == 1:
            print("Queda",intento,"intento")
        elif intento == 0:
            print("Ohhh, lo siento has perdido")
            seguir = False
    print("Fin del juego")

def calculo_iva ():
    

def selector ():
    salir = False
    while not salir:
        print("Selecciona entre las siguientes opciones")
        print("A: Piedra, Papel, Tijeras, Lagarto, Spock")
        print("B: Adivina el número")
        print("Exit: Teclea exit para salir")
        seleccion = input("¿Que quieres hacer? ")
        if seleccion == "A":
            piedra()
        elif seleccion == "B":
            adivina()
        elif seleccion == "Exit":
            print("¡Hasta luego!")
            salir = True
        else:
            print("La opcion introducida no existe")

selector()
