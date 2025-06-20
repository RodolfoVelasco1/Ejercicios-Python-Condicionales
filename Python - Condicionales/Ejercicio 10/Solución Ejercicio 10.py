# Solución Ejercicio 10
compra = float(input("Ingresa el monto de la compra: $"))

if compra > 1000:
    descuento = compra * 0.20
    total = compra - descuento
    print(f"Descuento del 20%: ${descuento:.2f}")
elif compra >= 500:
    descuento = compra * 0.10
    total = compra - descuento
    print(f"Descuento del 10%: ${descuento:.2f}")
elif compra >= 100:
    descuento = compra * 0.05
    total = compra - descuento
    print(f"Descuento del 5%: ${descuento:.2f}")
else:
    total = compra
    print("Sin descuento aplicable")

print(f"Total a pagar: ${total:.2f}")