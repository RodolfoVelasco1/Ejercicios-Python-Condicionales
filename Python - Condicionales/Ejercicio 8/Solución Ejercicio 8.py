# Solución Ejercicio 8
num1 = int(input("Ingresa el primer número: "))
operacion = input("Ingresa la operación (+, -, *, /): ")
num2 = int(input("Ingresa el segundo número: "))

if operacion == "+":
    resultado = num1 + num2
    print(f"{num1} + {num2} = {resultado}")
elif operacion == "-":
    resultado = num1 - num2
    print(f"{num1} - {num2} = {resultado}")
elif operacion == "*":
    resultado = num1 * num2
    print(f"{num1} * {num2} = {resultado}")
elif operacion == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"{num1} / {num2} = {resultado}")
    else:
        print("Error: No se puede dividir por cero")
else:
    print("Operación no válida")