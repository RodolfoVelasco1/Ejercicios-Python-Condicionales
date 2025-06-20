# Solución Ejercicio 13
contraseña = input("Ingresa una contraseña: ")

# Validamos la longitud primero
if len(contraseña) < 8:
    print("Contraseña inválida: debe tener al menos 8 caracteres.")
else:
    tiene_mayuscula = False
    tiene_numero = False

    for caracter in contraseña:
        if caracter >= "A" and caracter <= "Z":
            tiene_mayuscula = True
        if caracter >= "0" and caracter <= "9":
            tiene_numero = True

    if tiene_mayuscula and tiene_numero:
        print("Contraseña válida.")
    else:
        print("Contraseña inválida: debe tener al menos una letra mayúscula y un número.")