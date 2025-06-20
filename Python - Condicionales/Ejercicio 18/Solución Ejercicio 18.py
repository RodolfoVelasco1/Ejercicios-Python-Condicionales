# Solución Ejercicio 18
edad = int(input("Ingresa tu edad: "))
ingresos = float(input("Ingresa tus ingresos anuales: $"))
score = int(input("Ingresa tu score crediticio: "))

print("\n--- Evaluación de Préstamo ---")

edad_valida = 18 <= edad <= 65
ingresos_validos = ingresos >= 30000
score_valido = score >= 650

if edad_valida and ingresos_validos and score_valido:
    print("¡FELICIDADES! Calificas para el préstamo")
    
    # Determinar monto máximo según ingresos
    if ingresos >= 100000:
        monto_max = ingresos * 0.8
    elif ingresos >= 60000:
        monto_max = ingresos * 0.6
    else:
        monto_max = ingresos * 0.4
    
    print(f"Monto máximo aprobado: ${monto_max:,.2f}")
else:
    print("NO calificas para el préstamo.")
    print("Requisitos no cumplidos:")
    if not edad_valida:
        print("- Edad debe estar entre 18 y 65 años")
    if not ingresos_validos:
        print("- Ingresos mínimos de $30,000 anuales")
    if not score_valido:
        print("- Score crediticio mínimo de 650 puntos")