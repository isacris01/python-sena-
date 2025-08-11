vocales=(input("ingrese una vocal: "))
if vocales== "e" :
    print(f"la vocal {vocales} en mayusculas es E")
elif vocales=="a":
    print(f"la vocal {vocales} en mayusculas es A")
elif vocales=="i" :
    print(f"la vocal {vocales} en mayusculas es I")
elif vocales=="o" :
    print(f"la vocal {vocales} en mayusculas es O.")
elif vocales=="u" :
    print(f"la vocal {vocales} en mayusculas es U.")
else:
    print(f"{vocales} no es una vocal")
#EJEMPLO 1
comando="SALIR"
if comando=="ENTRAR":
    print("Bienvenido al sistema.")
elif comando=="SALUDO":
    print("Hola!¿como estas?")
elif comando=="SALIR":
    print("saliendo del sistma.")
else:
    print("no se reconoce el comando.")
#-------------------------------------EJERCICIO 1---------------------------------------------------
# Se solicita al usuario que ingrese un número
num=int(input("ingrese un numero: "))
# Se evalúa si el número es mayor que 0 (positivo)
if num>0:
    print(f"el numero {num} es positivo")
# Se evalúa si el número es exactamente 0
elif num==0:
    print(f"el numero {num} es 0 ")
# Se evalúa si el número es menor que 0 (negativo)
elif num<0:
    print(f"el numero {num} es negativo ")
else:
    print("esta opcion no es validad con las condicciones .")
#-------------------------------------EJERCICIO 2---------------------------------------------------
#Se solicita al usuario que ingrese los números
num=int(input("ingrese un numero: "))
num2=int(input("ingrese otro numero: "))
#Se compara si el primer número es mayor que el segundo
if num>num2:
    print(f"el numero mayor es {num}")
elif num2>num:
#Se compara si el segundo número es mayor que el primero
    print(f"el numero mayor es {num2}")
else:
    print("esta opcion no cumple con las condicciones .")
#-------------------------------------EJERCICIO 3---------------------------------------------------
#Determina si un número es par o impar.
num=int(input("ingrese un numero: "))
# Si el residuo de dividir el número entre 2 es 0, es par
if num % 2 == 0:
    print(f"El número {num} es par.")
else:
# Si no, es impar
    print(f"El número {num} es impar.")
#-------------------------------------EJERCICIO 4---------------------------------------------------
# Se solicita al usuario que ingrese un número
num=int(input("ingrese un numero: "))
# Se verifica si el número entre 10 y 20
if num>10 and num <20: 
    print(f"el numero {num} esta entre 10 y 20")
# Si no se cumple la condición, se muestra el siguente mensaje 
else:
    print(f"el numero {num} no esta entre 10 y 20")
#-------------------------------------EJERCICIO 5---------------------------------------------------
#Se solicita al usuario que ingrese los números
num=int(input("ingrese el primer numero: "))
num2=int(input("ingrese el segundo numero numero: "))
num3=int(input("ingrese el tercer numero numero: "))
# Comparamos si el primer número es mayor que los otros dos
if num >= num2 and num >= num3:
    print(f"El número mayor es: {num}")
# Si no, verificamos si el segundo número es mayor o igual que los otros dos
elif num2 >= num and num2 >= num3:
    print(f"El número mayor es: {num2}")
# Si ninguna de las anteriores se cumple, entonces el tercero es el mayor
else:
    print(f"El número mayor es: {num3}")
#-------------------------------------EJERCICIO 6---------------------------------------------------
# Se solicita al usuario el valor total de la compra
total=float(input("Ingrese el total de la compra: $"))
# Se evalúa si el total es mayor a $100
if total > 100:
# Se aplica un descuento del 10%
    descuento = total * 0.10
    precio_final = total - descuento
    print(f"Se aplicó un 10% de descuento. El precio final es: ${precio_final}")
else:
# Si no supera $100, no hay descuento
    print(f"No se aplica descuento. El precio final es: ${total}")
#-------------------------------------EJERCICIO 7---------------------------------------------------
#Se pide al usuario que ingrese su edad
edad=int(input("ingrese su edad: "))
#se verifica que sea igual o mayor de cero para que pueda votar
if edad>=18:
    print(f"su edad es {edad} y puede votar")
#si no,no puede votar
else:
    print(f"su edad es {edad} y NO puede votar")
#-------------------------------------EJERCICIO 8---------------------------------------------------
# Se solicita al usuario el precio del producto
precio=int(input("ingresa el precio del producto: "))
# Se solicita el tipo de cliente (VIP o normal)
tipo_cliente=input("ingresa el tipo de cliente(VIP o normal)")
# Se verifica si el cliente es VIP
if tipo_cliente == "VIP":
# Se calcula el descuento del 20%
    descuento = precio * 0.20
    precio_final = precio - descuento
    print(f"Cliente VIP: se aplicó un 20% de descuento. Precio final: ${precio_final:}")
else:
# Si no es VIP, no se aplica descuento
    print(f"Cliente normal: no hay descuento. Precio final: ${precio:}")
#-------------------------------------EJERCICIO 9---------------------------------------------------
# Se solicita al usuario que ingrese un número 
num=int(input("ingrese un numero: "))
# Se verifica si el número es multiplo de 5 y 3
if num % 5 == 0 and num % 3 == 0:
    print(f"El número {num} es múltiplo de 5 y de 3 al mismo tiempo.")
else:
    print(f"El número {num} NO es múltiplo de 5 y de 3 al mismo tiempo.")
#-------------------------------------EJERCICIO 10---------------------------------------------------
# Se solicita el número principal
num=int(input("ingrese un numero: "))
# Se solicitan los dos divisores
divi1=int(input("Ingrese el primer divisor: "))
divi2=int(input("Ingrese el segundo divisor: "))
# Se evalúa si el número es divisible entre ambos divisores
if num % divi1 == 0 and num % divi2 == 0:
    print(f"El número {num} es divisible entre {divi1} y {divi2}.")
#si no
else:
    print(f"El número {num} NO es divisible entre {divi1} y {divi2}.")
#-------------------------------------EJERCICIO 11---------------------------------------------------
# Se crea la lista con 5 números
numeros=[1,2,3,4,5]
# Se accede al tercer número
tercer_numeros =numeros[2]
# Se evalúa si el tercer número es mayor que 10
if tercer_numeros >= 10:
    print(f"el numero {tercer_numeros} es Mayor a 10")
else :
    print(f"el numero {tercer_numeros} es Menor a 10")
#-------------------------------------EJERCICIO 12---------------------------------------------------
# Se crea la lista pedida
numeros3=[3,5,7,9]
# Se extrae el número que está en la posición 2 (índice 2) de la lista
numero_7=numeros3[2]
# Se verifica si ese número es igual a 7
if numero_7 ==7: 
# Si es igual a 7, se muestra este mensaje
    print(f"El numero {numero_7} esta en la lista")
# Si no es igual a 7, se muestra este otro mensaje
else:
    print(f"El numero {numero_7} NO esta en la lista")
#-------------------------------------EJERCICIO 13---------------------------------------------------
#se crea la lista que nos piden
numeros=[4, 6, 2, 8]
# Se suman los dos primeros elementos (índices 0 y 1)
numero1=numeros[0]
numero2=numeros[1]
suma=numero1+numero2
# Se evalúa si la suma es mayor que 10
if suma>10:
    print(f"Suma alta por que es mayor que {suma}")
else:
    print(f"Suma baja por que es menor o igual a 10 que {suma}")
#-------------------------------------EJERCICIO 14---------------------------------------------------
#se crea la lista que nos pidieron
nombres=["Ana", "Luis", "Pedro", "Marta"]
# Se accede al último nombre de la lista usando índice -1
ultimo_nombre=nombres[-1]
# Se verifica si el último nombre es "Marta"
if ultimo_nombre=="Marta":
    print(f"el nombre {ultimo_nombre} Es correcto")
#si no que aparesca que es diferente
else:
    print(f"el nombre {ultimo_nombre} ES diferente")
#-------------------------------------EJERCICIO 15---------------------------------------------------
# Se piden los tres colores al usuario
color1=input("Ingrese el primer color: ")
color2=input("Ingrese el segundo color: ")
color3=input("Ingrese el tercer color: ")
# Se crea la lista
lista_colores=[color1, color2, color3]
# Se guarda el segundo color
segundo_color=lista_colores[1]
if segundo_color.lower()=="azul":
# Se actualiza el segundo elemento en la lista
    lista_colores[1] = "verde"
# Se muestra la lista actualizada
print("Lista actualizada:", lista_colores)
#-------------------------------------EJERCICIO 16---------------------------------------------------
#se crea la tupla
numeros=(5,8,12,20)
# Se accede al primer valor (índice 0) y al último valor (índice -1)
primer_valor=numeros[0]
ultimo_valor=numeros[-1]
# Se evalúa si el primer valor es menor que el último
if primer_valor < ultimo_valor:
    print("Orden ascendente")
else:
    print("Orden descendente")
#-------------------------------------EJERCICIO 17---------------------------------------------------
# Se creala la tupla que nos pidieron con tres edades
edades=(25,32,28)
# Se accede al segundo número de la tupla (índice 1)
segundo_num=edades[1]
# Se evalúa si el segundo número (edad) es mayor a 30
if segundo_num > 30:
    print("edad mayor a 30")
# Si la condición no se cumple, se muestra este otro mensaje
else:
    print("Edad menor o igual a 30")
#-------------------------------------EJERCICIO 18---------------------------------------------------
# Se define una tupla con los valores (1, 2, 3)
tupla_original=(1, 2, 3)
# Se convierte la tupla a lista para poder modificar sus elementos
lista_convertida=list(tupla_original)
# Se verifica si el segundo valor (índice 1) es igual a 2
if lista_convertida[1]==2:
# Si es igual a 2, se cambia ese valor a 10
    lista_convertida[1]=10
# Se convierte la lista nuevamente a tupla
tupla_modificada=tuple(lista_convertida)
# Se muestra la tupla final
print("Tupla modificada:", tupla_modificada)
#-------------------------------------EJERCICIO 19---------------------------------------------------
#se crea la tupla que nos dieron
numeros=(4, 9)
# Se obtiene el segundo valor de la tupla (índice 1)
segundo_valor=numeros[1]
# Se evalúa si el segundo valor es mayor que 5
if segundo_valor > 5:
    print("Coordenada alta")
# Si el valor es menor o igual a 5, se muestra este mensaje
else:
    print("Coordenada baja")
#-------------------------------------EJERCICIO 20---------------------------------------------------
#se crean las dos tuplas que nos pidieron
tupla1=(3, 4)
tupla2=(3, 5)
#se verifica si las dos tuplas son iguales
if tupla1==tupla2 :
#si lo son muestra el siguiente mensaje
    print("Tuplas iguales")
#si no,muestra este otro mensaje
else:
    print("Tuplas diferentes")
#-------------------------------------EJERCICIO 21---------------------------------------------------
#creamos el diccionario que nos piden
edad1={
    "nombre": "Juan",
    "edad": 17
}
#Se evalúa si el valor asociado a la clave "edad" es mayor o igual a 18
if edad1["edad"] >= 18:
# Si la condición es verdadera, se imprime "Adulto"
    print("Adulto")
# Si la condición es falsa,se imprime "Menor de edad"
else:
   print("Menor de edad")
#-------------------------------------EJERCICIO 22---------------------------------------------------
#creamos el diccionario que nos piden
datos={
    "nombre":"Lucía", 
    "edad": 20
}
# Se evalúa si la edad es mayor a 18
if datos["edad"] >18:
# Si es mayor, se actualiza el valor de "edad" a 21
    datos["edad"] =21
# Se muestra el diccionario final
print(datos)
#-------------------------------------EJERCICIO 23---------------------------------------------------
# Se crea el diccionario que nos pidieron
persona={
    "nombre": "Carlos"
}
# Se verifica si la clave "ciudad" no está en el diccionario
if "ciudad" not in persona:
    # Si no existe, se agrega con el valor "Bogotá"
    persona["ciudad"] = "Bogotá"
# Se muestra el diccionario actualizado
print(persona)
#-------------------------------------EJERCICIO 24---------------------------------------------------
#se crea el diccionario que nos pidieron
producto={
    "producto": "pan",
    "precio": 1200
}
# Se verifica si la clave "precio" está en el diccionario
if "precio" in producto :
# Si existe, se muestra su valor
    print(producto["precio"])
# Si no existe, se muestra un mensaje alternativo
else:
    print("No hay precio")
#-------------------------------------EJERCICIO 25---------------------------------------------------
#creo el diccionario que me pidieron con los productos
productos={
    "pan": 1200,
    "leche": 2000
}
#verifico que el producto pan este en el diccionario
if "pan" in productos:
#Si pan está en el diccionario muestra el precio
    print(productos["pan"])
#si no muestro el siguiente mensaje
else:
    print("Producto no disponible")


