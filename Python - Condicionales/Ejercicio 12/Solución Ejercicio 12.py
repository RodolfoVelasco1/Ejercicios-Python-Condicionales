# Solución Ejercicio 12
import random

numero_secreto = random.randint(1, 10)
intento = int(input("Adivina el número del 1 al 10: "))

if intento == numero_secreto:
    print("¡Felicidades! Adivinaste el número")
elif intento > numero_secreto:
    print(f"Muy alto. El número era {numero_secreto}")
else:
    print(f"Muy bajo. El número era {numero_secreto}")