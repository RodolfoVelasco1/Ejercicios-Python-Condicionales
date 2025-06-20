# Solución Ejercicio 16
edad = int(input("Ingresa la edad: "))

if edad < 0:
    print("Edad inválida")
elif edad <= 2:
    print("Clasificación: Bebé")
elif edad <= 12:
    print("Clasificación: Niño")
elif edad <= 17:
    print("Clasificación: Adolescente")
elif edad <= 35:
    print("Clasificación: Adulto joven")
elif edad <= 65:
    print("Clasificación: Adulto")
else:
    print("Clasificación: Adulto mayor")