
numero1=float(input("ingrese un numero:"))
if numero1 > 0:
    print("positivo.")
elif numero1 < 0 :
    print(f"es negativo por que es{numero1}")
else:
    print(f"es cero{numero1}")
#2 .Calcular el mayor de dos numeros ingresados
num1=float(input("ingrese un numero:"))
num2=float(input("ingrese otro numero.:"))
if num1>num2:
    print(f"el numero mayor es {num1}")
elif num2>num1:
    print(f"el numero ayor es {num2}")
else:
    print(f"ambos numeros son iguales.")
#-----------------------------------EJERCICIOS CON CONDICIONALES Y OPERACIONES MATEMATICAS-----------------
#----------------------------------------EJERCICIO 1-------------------------------------------------
numero1=float(input("ingrese un numero:"))
if numero1 > 0:
    print("positivo")
elif numero1 < 0 :
    print(f"es negativo por que es{numero1}")
else:
    print(f"es cero{numero1}")
#----------------------------------------EJERCICIO 2-------------------------------------------------
num1=float(input("ingrese un numero:"))
num2=float(input("ingrese otro numero:"))
if num1>num2:
    print(f"el numero mayor es {num1}")
elif num2>num1:
    print(f"el numero ayor es {num2}")
else:
    print(f"ambos numeros son iguales.")
#----------------------------------------EJERCICIO 3-------------------------------------------------
numero=float(input("ingrese un numero:"))
if numero % 2 == 0:
    print("El numero es par: ")
else:
    print("el numero es impar")
#----------------------------------------EJERCICIO 4-------------------------------------------------
numero2=float(input("ingrese un numero:"))
if 10<=numero2 <=20 :
    print(f"el numero {numero2} esta entre 10 y 20 ")
else:
    print(f"el numero {numero2} NO esta entre 10 y 20")
#----------------------------------------EJERCICIO 5-------------------------------------------------
num1=float(input("ingrese el primer numero:"))
num2=float(input("ingrese el segundo numero:"))
num3=float(input("ingrese el tercer numero:"))
if num1>num2 and num1>num3:
    print(f"el numero mayor es {num1}")
elif num2>num1 and num2>num3:
    print(f"el numero mayor es {num2}")
else:
    print(f"el numero mayor es {num3}")
#----------------------------------------EJERCICIO 6-------------------------------------------------
precio=float(input("Ingresa el precio: "))
if precio > 100:
    descuento=precio * 0.10
    total_final=precio - descuento
else:
    total_final=precio
print("El precio final es:", total_final)
#----------------------------------------EJERCICIO 7-------------------------------------------------
edad=float(input("ingrese su edad:"))
if edad>= 18:
    print("puede votar por que es mayor de edad ")
else:
    print("no puede votar,por que es menor de edad")
#----------------------------------------EJERCICIO 8-------------------------------------------------
precio=float(input("Ingresa el precio: "))
tipo=input("Ingresa el tipo de cliente (VIP o normal): ")
if tipo=="VIP":
    precio_final=precio * 0.80
else:
    precio_final=precio
print("El precio final es:", precio_final)
#----------------------------------------EJERCICIO 9-------------------------------------------------
numero=int(input("Ingresa un número: "))
if numero % 5 == 0 and numero % 3 == 0:
    print(f"El numero {numero} es un múltiplo de 5 y de 3.")
else:
    print(f"El numero {numero},No es múltiplo de 5 y de 3 al mismo tiempo.")
#----------------------------------------EJERCICIO 10-------------------------------------------------
numero=int(input("Ingresa el número: "))
div1=int(input("Ingresa el primer divisor: "))
div2=int(input("Ingresa el segundo divisor: "))
if numero % div1 == 0 and numero % div2 == 0:
    print(f"El número es divisible entre {div1} y {div2}.")
else:
    print(f"El número NO es divisible entre {div1} y {div2}.")
#------------------------TALLER DE CONDICIONALES,INTERACCION Y ESTRUCTURAS DE DATOS-----------------------
#----------------------------------------EJERCICIO 1--------------------------------------------------
edad=float(input("ingrese su edad:"))
if edad<= 18:
    print("Eres menor de edad ")
elif edad>  65:
    print("Eres un adulto mayor ")
else:
    print("Eres mayor de edad")
#----------------------------------------EJERCICIO 2--------------------------------------------------
Estatura=float(input("ingrese tu estatura en metros (ej:1.50):"))
if Estatura < 1.5:
    print("Eres considerado bajo")
elif 1.5 <= Estatura <= 1.8:
    print("Tienes Estatura media")
else:
    print("Eres considerado alto")
#----------------------------------------EJERCICIO 3--------------------------------------------------
numero=int(input("ingrese un numero:"))
if numero % 2 == 0 and numero % 3 == 0:
    print(f"El numero {numero} es multiplo de 2 y 3.")
elif numero % 2 == 0 :
    print(f"El numero {numero} es multiplo de 2.")
elif numero % 3 == 0:
    print(f"El numero {numero} es multiplo de 3.")
else:
    print(f"el numero {numero}  no es multiplo de 2 ni de 3")
#----------------------------------------EJERCICIO 4-------------------------------------------------
numero=input("Ingresa un número decimal: ")
partes=numero.split(".")
if len(partes) == 2:
    decimales = len(partes[1])
    if decimales == 1:
        print(f"El número {numero} iene 1 decimal.")
    elif decimales == 2:
        print(f"El número {numero} iene 2 decimales.")
    else:
        print(f"El número {numero} tiene más de 2 decimales.")
else:
    print(f"El número {numero} no tiene parte decimal.")
#----------------------------------------EJERCICIO 5-------------------------------------------------
paises=("Colombia", "Perú", "Argentina", "México")
pais=input("Ingresa un país: ")
if pais in paises:
    print(f"{pais} está en la lista.")
else:
    print(f"{pais} no está en la lista.")
#----------------------------------------EJERCICIO 6-------------------------------------------------
compatibilidad={
    "A":["A", "AB"],
    "B":["B", "AB"],
    "AB":["AB"],
    "O":["A", "B", "AB", "O"]
}
tipo=input("Ingresa tu tipo de sangre (A, B, AB, O): ").upper()
if tipo in compatibilidad:
    print(f"Puedes donar a: {', '.join(compatibilidad[tipo])}")
else:
    print("Tipo de sangre no reconocido.")
#----------------------------------------EJERCICIO 7-------------------------------------------------
temp=float(input("Ingresa la temperatura en °C: "))
if temp < 10:
    print("Hace frío.")
elif 10 <=temp <=25:
    print("Está templado.")
else:
    print("Hace calor.")
#----------------------------------------EJERCICIO 8-------------------------------------------------
print("Menú de operaciones:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
opcion=input("Elige una opción (1, 2 o 3): ")
num1=float(input("Ingresa el primer número: "))
num2=float(input("Ingresa el segundo número: "))
if opcion == "1":
    print(f"Resultado de la suma : {num1 + num2}")
elif opcion == "2":
    print(f"Resultado de la resta : {num1 - num2}")
elif opcion == "3":
    print(f"Resultado de la multiplicacion : {num1 * num2}")
else:
    print("Opción no válida.")
#----------------------------------------EJERCICIO 9-------------------------------------------------
meses={
    1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril",
    5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
    9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
}
numero=int(input("Ingresa un número entre 1 y 12: "))
if 1<=numero <=12:
    print(f"El mes correspondiente es: {meses[numero]}")
else:
    print("Número fuera de rango.")
#----------------------------------------EJERCICIO 10-------------------------------------------------
numero=input("Ingresa un número de 4 dígitos: ")
if len(numero)==4 and numero.isdigit():
    if numero.startswith("1"):
        print("Empieza con 1.")
    elif numero.startswith("2"):
        print("Empieza con 2.")
    else:
        print("Empieza con otro número.")
else:
    print("No ingresaste un número válido de 4 dígitos.")
#----------------------------------------EJERCICIO 11-----------------------------------------------
entrada=input("Ingresa una palabra: ")
if entrada:
    primera=entrada[0]

    if primera.isdigit():
        print("La primera letra es un número.")
    elif primera.lower() in "aeiou":
        print("La primera letra es una vocal.")
    elif primera.isalpha():
        print("La primera letra es una consonante.")
    else:
        print("La primera letra no es válida.")
else:
    print("No ingresaste una palabra.")
#----------------------------------------EJERCICIO 12----------------------------------------------
frutas={
    "manzana": 2500,
    "pera": 2200,
    "piña": 3200
}
fruta=input("Ingresa una fruta: ").lower()
if fruta in frutas:
    print(f"El precio de la {fruta} es ${frutas[fruta]}")
else:
    print("La fruta no está disponible.")
#----------------------------------------EJERCICIO 13---------------------------------------------
calificacion=float(input("Ingresa tu calificación (0 a 5): "))
if 0 <= calificacion <= 5:
    if calificacion < 3:
        print("Reprobado.")
    elif 3 <= calificacion <= 4:
        print("Aprobado.")
    else:
        print("Excelente.")
else:
    print("Calificación fuera de rango.")
#----------------------------------------EJERCICIO 14--------------------------------------------
numero=int(input("Ingresa un número: "))
if numero % 4==0 and numero % 6 == 0:
    print(f"El numero {numero} es divisible entre 4 y entre 6.")
elif numero % 4==0:
    print(f"El numero {numero} es divisible entre 4.")
elif numero % 6==0:
    print(f"El numero {numero} es divisible entre 6.")
else:
    print(f"El numero {numero} no es divisible entre 4 ni entre 6.")
#----------------------------------------EJERCICIO 15--------------------------------------------
usuarios={
    "Isabel": "101009",
    "Estefeni": "2018",
    "Wilson": "Isabel2009"
}
usuario=input("Usuario: ")
clave=input("Clave: ")
if usuario in usuarios and usuarios[usuario]==clave:
    print("Acceso concedido.")
else:
    print("Usuario o clave incorrectos.")
#----------------------------------------EJERCICIO 16--------------------------------------------
edad=int(input("Ingresa tu edad: "))
if 0 <= edad <= 12:
    print("Eres un niño.")
elif 13 <= edad <= 17:
    print("Eres un adolescente.")
elif 18 <= edad <= 64:
    print("Eres un adulto.")
elif edad >= 65:
    print("Eres un adulto mayor.")
else:
    print("Edad no válida.")
#----------------------------------------EJERCICIO 17--------------------------------------------
capitales=("Madri", "Lima", "Buenos Aires", "Ciudad de México")
ciudad=input("Ingresa el nombre de una ciudad: ")
if ciudad in capitales:
    print(f"{ciudad} es una capital.")
else:
    print(f"{ciudad} es una ciudad secundaria.")
#----------------------------------------EJERCICIO 18--------------------------------------------
valor=float(input("Ingresa el valor de la compra: "))
if valor > 200000:
    descuento=valor * 0.15
    total=valor - descuento
    print(f"Aplica 15% de descuento. Total a pagar: ${total:.0f}")
elif 100000 <= valor <= 200000:
    descuento = valor * 0.10
    total = valor - descuento
    print(f"Aplica 10% de descuento. Total a pagar: ${total:.0f}")
else:
    print(f"No hay descuento. Total a pagar: ${valor:.0f}")
#----------------------------------------EJERCICIO 19--------------------------------------------
nombre=input("Ingresa tu nombre: ")
horas=float(input("Ingresa el número de horas trabajadas: "))
tarifa=10000
salario_base=horas*tarifa
if horas > 40:
    bono=salario_base*0.20
    salario_total=salario_base+bono
    print(f"{nombre}, tu salario es ${salario_total:.0f} (incluye bono del 20%).")
else:
    print(f"{nombre}, tu salario es ${salario_base:.0f}.")
#----------------------------------------EJERCICIO 20--------------------------------------------
puntaje=int(input("Ingresa tu puntaje (0 a 100): "))
if puntaje <50:
    print(f"Tu puntaje es {puntaje},es decir Insuficiente.")
elif 50 <=puntaje <= 79:
    print(f"Tu puntaje es {puntaje},es decir Aceptable.")
elif 80 <=puntaje <= 100:
    print(f"Tu puntaje es {puntaje},es decir Sobresaliente.")
else:
    print("Puntaje fuera de rango.")
    







    

    















