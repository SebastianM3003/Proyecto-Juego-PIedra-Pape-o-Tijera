import random # esta función permite que la PC pueda elegir una opción al azar 

opcion_usuario = 0
puntos_usuario = 0
puntos_pc = 0

# inciamos con el bucle o loop del programa
while opcion_usuario != 4:
    print("*** NUEVA RONDA ***")
    opcion_usuario = int(input("Elige estas opciones para jugar: 1. Piedra, 2. Papel, 3. Tijera, 4. Salir: "))
    if opcion_usuario == 4:
        continue
    if opcion_usuario >= 1 and opcion_usuario <= 3:
        opcion_pc = random.randint(1,3) # esta función "randon.randint()" permite que la pc elija su opción
        print("La computadora eligió la opción: " + str(opcion_pc))
        if opcion_usuario == opcion_pc:
            print("¡Es un empate!, ambos eligieron lo mismo")
        elif (opcion_usuario == 1 and opcion_pc == 3) or (opcion_usuario == 2 and opcion_pc == 1) or (opcion_usuario == 3 and opcion_pc == 2):
            print("¡Ganaste esta ronda!")
            puntos_usuario = puntos_usuario + 1 # acumulamos puntuación en el caso de que gane usuario
        else:
            puntos_pc = puntos_pc + 1  # acumula puntuación en el caso de que gane PC
        print("Marcador actual ---->> Tú: " + str(puntos_usuario) + "  //  PC: " + str(puntos_pc))
    else:
        print("Opción no válida. Por favor, elige un número del 1 al 4")

print("Gracias por jugar, nos vemos a la próxima")


