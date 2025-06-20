# Solución Ejercicio 20
print("=== SISTEMA DE RESERVAS DE HOTEL ===")

# Tipo de habitación
print("Tipos de habitación:")
print("1. Simple - $100 por noche")
print("2. Doble - $150 por noche")
print("3. Suite - $300 por noche")
tipo_hab = int(input("Selecciona tipo de habitación (1-3): "))

# Temporada
print("\nTemporadas:")
print("1. Temporada Alta (+50%)")
print("2. Temporada Media (+25%)")
print("3. Temporada Baja (precio base)")
temporada = int(input("Selecciona temporada (1-3): "))

dias = int(input("Ingresa número de días de estadía: "))

# Definir precio base
if tipo_hab == 1:
    precio_base = 100
    tipo_nombre = "Simple"
elif tipo_hab == 2:
    precio_base = 150
    tipo_nombre = "Doble"
elif tipo_hab == 3:
    precio_base = 300
    tipo_nombre = "Suite"
else:
    print("Tipo de habitación inválido")
    exit()

# Aplicar modificador de temporada
if temporada == 1:
    precio_noche = precio_base * 1.5
    temp_nombre = "Alta"
elif temporada == 2:
    precio_noche = precio_base * 1.25
    temp_nombre = "Media"
elif temporada == 3:
    precio_noche = precio_base
    temp_nombre = "Baja"
else:
    print("Temporada inválida")
    exit()

# Calcular subtotal
subtotal = precio_noche * dias

# Aplicar descuento por estadía larga
if dias >= 14:
    descuento = subtotal * 0.25
    desc_porcentaje = "25%"
elif dias >= 7:
    descuento = subtotal * 0.15
    desc_porcentaje = "15%"
else:
    descuento = 0
    desc_porcentaje = "0%"

total = subtotal - descuento

# Mostrar resumen
print("\n" + "="*40)
print("RESUMEN DE RESERVA")
print("="*40)
print(f"Habitación: {tipo_nombre}")
print(f"Temporada: {temp_nombre}")
print(f"Días de estadía: {dias}")
print(f"Precio por noche: ${precio_noche:.2f}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Descuento ({desc_porcentaje}): ${descuento:.2f}")
print(f"TOTAL A PAGAR: ${total:.2f}")
print("="*40)