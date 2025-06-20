# Solución Ejercicio 5
calificacion = float(input("Ingresa tu calificación (0-100): "))

if calificacion >= 90:
    print("Tu calificación es: A")
elif calificacion >= 80:
    print("Tu calificación es: B")
elif calificacion >= 70:
    print("Tu calificación es: C")
elif calificacion >= 60:
    print("Tu calificación es: D")
else:
    print("Tu calificación es: F")