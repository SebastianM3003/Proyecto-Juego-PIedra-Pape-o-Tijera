import random

def mostrar_bienvenida():
    """Muestra el mensaje inicial del juego."""
    print("=========================================")
    print("      ¡BIENVENIDO A PIEDRA, PAPEL O TIJERA!  ")
    print("=========================================")

def obtener_opcion_computadora():
    """Selecciona de forma aleatoria la opción de la IA."""
    opciones = ["piedra", "papel", "tijera"]
    return random.choice(opciones)

def jugar():
    mostrar_bienvenida()
    
    # Estructura repetitiva (Bucle) para mantener el juego activo
    # Cumple con el requisito de usar bucles del Paso 2
    jugando = True
    while jugando:
        print("\nElige una opción:")
        print("1. Piedra")
        print("2. Papel")
        print("3. Tijera")
        print("4. Salir del juego")
        
        opcion_usuario = input("Ingresa el número de tu elección: ").strip()
        
        # Estructuras lógicas condicionales (Validación y lógica del juego)
        if opcion_usuario == "4":
            print("\n¡Gracias por jugar! Hasta la próxima.")
            jugando = False
            break
            
        elif opcion_usuario in ["1", "2", "3"]:
            # Mapeo de la selección del usuario
            mapa_opciones = {"1": "piedra", "2": "papel", "3": "tijera"}
            eleccion_usuario = mapa_opciones[opcion_usuario]
            eleccion_computadora = obtener_opcion_computadora()
            
            print(f"\nTú elegiste: {eleccion_usuario.capitalize()}")
            print(f"La computadora eligió: {eleccion_computadora.capitalize()}")
            
            # Condicionales para determinar el ganador de la ronda
            if eleccion_usuario == eleccion_computadora:
                print("¡Es un empate!")
            elif (eleccion_usuario == "piedra" and eleccion_computadora == "tijera") or \
                 (eleccion_usuario == "papel" and eleccion_computadora == "piedra") or \
                 (eleccion_usuario == "tijera" and eleccion_computadora == "papel"):
                print("¡Ganaste esta ronda! 🎉")
            else:
                print("La computadora gana esta ronda. 🤖")
        else:
            print("Opción no válida. Por favor, ingresa 1, 2, 3 o 4.")

# Punto de entrada del programa
if __name__ == "__main__":
    jugar()