# Solución Ejercicio 15
print("Conversor de Temperatura")
print("1. Celsius a Fahrenheit")
print("2. Celsius a Kelvin")
print("3. Fahrenheit a Celsius")
print("4. Fahrenheit a Kelvin")
print("5. Kelvin a Celsius")
print("6. Kelvin a Fahrenheit")

opcion = int(input("Elige una opción (1-6): "))
temperatura = float(input("Ingresa la temperatura: "))

if opcion == 1:
    resultado = (temperatura * 9/5) + 32
    print(f"{temperatura}°C = {resultado:.2f}°F")
elif opcion == 2:
    resultado = temperatura + 273.15
    print(f"{temperatura}°C = {resultado:.2f}K")
elif opcion == 3:
    resultado = (temperatura - 32) * 5/9
    print(f"{temperatura}°F = {resultado:.2f}°C")
elif opcion == 4:
    resultado = (temperatura - 32) * 5/9 + 273.15
    print(f"{temperatura}°F = {resultado:.2f}K")
elif opcion == 5:
    resultado = temperatura - 273.15
    print(f"{temperatura}K = {resultado:.2f}°C")
elif opcion == 6:
    resultado = (temperatura - 273.15) * 9/5 + 32
    print(f"{temperatura}K = {resultado:.2f}°F")
else:
    print("Opción no válida")