#------------------------------------EJERCICIO 1----------------------------
"""# Ejercicio 1: Suma hasta cero
total = 0  # # Acumulador para la suma
numero = int(input("Ingresa un número entero (0 para terminar): "))#Pedimos al usuario que ingrese un número entero.
while numero != 0: # Mientras no se ingrese 0
    total += numero #Sumamos el número ingresado al 'total'.
    numero = int(input("Ingresa otro número (0 para terminar): "))

print("La suma total es:", total)
#------------------------------------EJERCICIO 2----------------------------
clave_correcta = "python123"# Guardamos la contraseña correcta
clave = input("Escribe la contraseña: ")#Pedimos al usuario que ingrese una contraseña.
while clave != clave_correcta: # Mientras no coincida, repetimos.
    print("Contraseña incorrecta, intenta de nuevo.")#Informamos al usuario que la contraseña es incorrecta.
    clave = input("Escribe la contraseña: ")#Volvemos a pedir la contraseña.
print("¡Contraseña correcta! Acceso concedido.")"""#Si la contraseña es correcta, salimos del bucle y mostramos el mensaje.
#------------------------------------EJERCICIO 3----------------------------
lista_compras = [] # se crea una lista vacía para guardar productos.
producto = input("\nAgrega un producto (o escribe 'fin' para terminar): ")#Pedimos al usuario que escriba el primer producto.
while producto.lower() != "fin": #Mientras el usuario NO escriba "fin", seguimos pidiendo productos.
    lista_compras.append(producto)#Agregar producto a la lista.
    producto = input("Agrega otro producto (o escribe 'fin' para terminar): ")#Pedir el siguiente producto.
print("\nLista de compras:", lista_compras)#Mostrar la lista completa de compras.
#------------------------------------EJERCICIO 4----------------------------
