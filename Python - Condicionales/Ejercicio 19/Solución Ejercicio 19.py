# Solución Ejercicio 19
import random

opciones = ["piedra", "papel", "tijeras"]
computadora = random.choice(opciones)

print("=== PIEDRA, PAPEL O TIJERAS ===")
jugador = input("Elige piedra, papel o tijeras: ").lower()

if jugador not in opciones:
    print("Opción inválida")
else:
    print(f"Tú elegiste: {jugador}")
    print(f"Computadora eligió: {computadora}")
    
    if jugador == computadora:
        print("¡EMPATE!")
    elif (jugador == "piedra" and computadora == "tijeras") or \
         (jugador == "papel" and computadora == "piedra") or \
         (jugador == "tijeras" and computadora == "papel"):
        print("¡GANASTE!")
    else:
        print("¡PERDISTE!")