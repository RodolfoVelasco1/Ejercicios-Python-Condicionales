# Solución Ejercicio 9
lado1 = float(input("Ingresa la longitud del primer lado: "))
lado2 = float(input("Ingresa la longitud del segundo lado: "))
lado3 = float(input("Ingresa la longitud del tercer lado: "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print("Las longitudes pueden formar un triángulo válido")
else:
    print("Las longitudes NO pueden formar un triángulo válido")