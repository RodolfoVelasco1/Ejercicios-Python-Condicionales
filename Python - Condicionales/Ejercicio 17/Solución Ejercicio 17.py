# Solución Ejercicio 17
precio = float(input("Ingresa el precio del producto: $"))
print("Tipos de producto:")
print("1. Alimentos")
print("2. Medicina")
print("3. Otros")
tipo = int(input("Selecciona el tipo de producto (1-3): "))

if tipo == 1:
    iva = precio * 0.105
    tasa = "10.5%"
elif tipo == 2:
    iva = 0
    tasa = "0%"
elif tipo == 3:
    iva = precio * 0.21
    tasa = "21%"
else:
    print("Tipo de producto inválido")
    exit()

total = precio + iva

print(f"Precio base: ${precio:.2f}")
print(f"IVA ({tasa}): ${iva:.2f}")
print(f"Total: ${total:.2f}")