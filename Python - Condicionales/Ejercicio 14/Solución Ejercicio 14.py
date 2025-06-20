# Solución Ejercicio 14
nota1 = float(input("Ingresa la primera nota: "))
nota2 = float(input("Ingresa la segunda nota: "))
nota3 = float(input("Ingresa la tercera nota: "))

promedio = (nota1 + nota2 + nota3) / 3

print(f"Promedio: {promedio:.2f}")

if promedio >= 6:
    print("Estado: APROBADO")
elif promedio >= 4:
    print("Estado: DEBE RECUPERAR")
else:
    print("Estado: DESAPROBADO")