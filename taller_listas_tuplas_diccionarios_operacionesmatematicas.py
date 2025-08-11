#-------------------------------------------EJERCICIO 1-------------------------------------------------
nota1=int(input("ingresa la primera calificacion: "))
nota2=int(input("ingresa la segunda calificacion: "))
nota3=int(input("ingresa la tercera calificacion: "))
lista=[nota1,nota2,nota3]
print(lista)
promedio=nota1+nota2+nota3/3
print(f"El promedio de las calificaciones es: {promedio}")
#-------------------------------------------EJERCICIO 2-------------------------------------------------
productos={
    "lapiz": 1000,
    "borrador": 800,
    "cuaderno":2200
}
print(productos)
porcentaje=float(input("ingrese el porcentaje de aumento(%): "))
productos["lapiz"]+=productos["lapiz"]*(porcentaje/100)
productos["borrador"]+=productos["borrador"]*(porcentaje/100)
productos["cuaderno"]+=productos["cuaderno"]*(porcentaje/100)
print(productos)
#-------------------------------------------EJERCICIO 3-------------------------------------------------
tem1=float(input("temperatura 1 en °c: "))
tem2=float(input("temperatura 2 en °c: "))
tem3=float(input("temperatura 3 en °c: "))
tem4=float(input("temperatura 4 en °c: "))
tem5=float(input("temperatura 5 en °c: "))
celsius=(tem1,tem2,tem3,tem4,tem5)
f1=tem1*9/5+32
f2=tem2*9/5+32
f3=tem3*9/5+32
f4=tem4*9/5+32
f5=tem5*9/5+32
fahrenheit=(f1,f2,f3,f4,f5)
print("temperaturas en °c:",celsius)
print("temperaturas en °F:",fahrenheit)
#-------------------------------------------EJERCICIO 4-------------------------------------------------
edades=[int(input("ingresa la primera edad: ")),int(input("ingresa la segunda edad: ")),int(input("ingresa la tercera edad: ")),int(input("ingresa la cuarta edad: ")),int(input("ingresa la quinta edad: "))]
promedio=sum(edades)/len(edades)
print(f"Mayor: {max(edades)},Menor: {min(edades)},promedio: {promedio}")
#-------------------------------------------EJERCICIO 5-------------------------------------------------
frutas={
    "sandia":3000,
    "fresa":2500,
    "banano":2800
}
print(frutas)
total=0
for fruta,precio in frutas.items():
    kilos=float(input(f"cuantos kilos  de {fruta} quieres?(${precio}por kilo:"))
total2=kilos*precio
print(f"el precio total a pagar ${total2:.2f}")
#-------------------------------------------EJERCICIO 6-------------------------------------------------
num1=int(input("ingresa un numero: "))
num2=int(input("ingresa otro numero: "))
num3=int(input("ingresa otro numero: "))
num4=int(input("ingresa otro numero: "))
num5=int(input("ingresa otro numero: "))
numeros=(num1,num2,num3,num4,num5)
suma=sum(numeros)
print(f"tupla ingresada: ",numeros)
print(f"suma total de los numeros: ",suma)
#-------------------------------------------EJERCICIO 7-------------------------------------------------
inventario=[]
for i in range(3):
    nombre=input(f"Ingrese el nombre del producto {i+1}: ")
    cantidad=int(input(f"Ingrese la cantidad de {nombre}: "))
    precio=float(input(f"Ingrese el precio de {nombre}: "))
    producto={"nombre": nombre, "cantidad": cantidad, "precio": precio}
    inventario.append(producto)
total=sum(item["cantidad"]*item["precio"] for item in inventario)
print(f"Total del inventario: $, {total}")
#-------------------------------------------EJERCICIO 8-------------------------------------------------
p1=int(input("Ingrese el primer precio: "))
p2=int(input("Ingrese el segundo precio: "))
p3=int(input("Ingrese el tercer precio: "))
p4=int(input("Ingrese el cuarto precio: "))
p5=int(input("Ingrese el quinto precio: "))
precios=[p1, p2, p3, p4, p5]
descuento=int(input("Ingrese el descuento en porcentaje (%): "))
nuevo1=p1-(p1*descuento/100)
nuevo2=p2-(p2*descuento/100)
nuevo3=p3-(p3*descuento/100)
nuevo4=p4-(p4*descuento/100)
nuevo5=p5-(p5*descuento/100)
precios_descuento=[nuevo1, nuevo2, nuevo3, nuevo4, nuevo5]
print(f"Precios originales:, {precios}")
print(f"Precios con descuento:, {precios_descuento}")
#-------------------------------------------EJERCICIO 9-------------------------------------------------
nota1=float(input("Ingrese la primera nota: "))
nota2=float(input("Ingrese la segunda nota: "))
nota3=float(input("Ingrese la tercera nota: "))
nota4=float(input("Ingrese la cuarta nota: "))
notas=(nota1, nota2, nota3, nota4)
nota_mayor=max(notas)
nota_menor=min(notas)
print(f"Notas ingresadas:, {notas}")
print(f"Nota más alta:, {nota_mayor}")
print(f"Nota más baja:, {nota_menor}")
#-------------------------------------------EJERCICIO 10-------------------------------------------------
medidas= {
    "km": 1000,
    "m": 1,
    "cm": 0.01
}
print(medidas)
unidad=input("Escribe la unidad (km, m o cm): ")
cantidad=float(input("Escribe la cantidad a convertir: "))
if unidad=="km":
    resultado=cantidad * 1000
elif unidad=="m":
    resultado=cantidad * 1
elif unidad=="cm":
    resultado=cantidad * 0.01
else:
    resultado=None
    print("Unidad no válida")
if resultado is not None:
    print("Equivale a", resultado, "metros.")
#-------------------------------------------EJERCICIO 11-------------------------------------------------
precio1=float(input("Precio del primer producto: "))
precio2=float(input("Precio del segundo producto: "))
precio3=float(input("Precio del tercer producto: "))
precio1_iva=precio1 + (precio1 * 0.19)
precio2_iva=precio2 + (precio2 * 0.19)
precio3_iva=precio3 + (precio3 * 0.19)
print(f"Precio 1 con IVA:, {precio1_iva}")
print(f"Precio 2 con IVA:, {precio2_iva}")
print(f"Precio 3 con IVA:, {precio3_iva}")
#-------------------------------------------EJERCICIO 12-------------------------------------------------
num1=float(input("Primer número: "))
num2=float(input("Segundo número: "))
suma=num1+num2
resta=num1-num2
multiplicacion=num1*num2
if num2 != 0:
    division = num1/num2
else:
    division="No se puede dividir entre cero"
resultados=(suma, resta, multiplicacion, division)
print(f"Resultados:, {resultados}")
#----------------------------------------------EJERCICIO 13-----------------------------------
nombre1=input("Nombre del primer estudiante: ")
nota1=float(input("Nota de " + nombre1 + ": "))
nombre2=input("Nombre del segundo estudiante: ")
nota2=float(input("Nota de " + nombre2 + ": "))
nombre3=input("Nombre del tercer estudiante: ")
nota3=float(input("Nota de " + nombre3 + ": "))
estudiantes={
    nombre1: nota1,
    nombre2: nota2,
    nombre3: nota3
}
print(estudiantes)
promedio=(nota1 + nota2 + nota3)/3
print(f"Notas de los estudiantes:, {estudiantes}")
print(f"Promedio general:, {promedio}")
#-------------------------------------------EJERCICIO 14------------------------------------------
salario1 = float(input("Ingrese el primer salario: "))
salario2 = float(input("Ingrese el segundo salario: "))
salario3 = float(input("Ingrese el tercer salario: "))
salario4 = float(input("Ingrese el cuarto salario: "))
salario5 = float(input("Ingrese el quinto salario: "))
salarios = [salario1, salario2, salario3, salario4, salario5]
nuevo1 = salario1 + (salario1 * 0.10)
nuevo2 = salario2 + (salario2 * 0.10)
nuevo3 = salario3 + (salario3 * 0.10)
nuevo4 = salario4 + (salario4 * 0.10)
nuevo5 = salario5 + (salario5 * 0.10)
salarios_nuevos = [nuevo1, nuevo2, nuevo3, nuevo4, nuevo5]
print(f"Salarios con aumento del 10%:, {salarios_nuevos}")
#-----------------------------------------ejercicio 15--------------------------------------------
producto1 = input("Nombre del primer producto: ")
precio1 = float(input("Precio sin impuesto de " + producto1 + ": "))
producto2 = input("Nombre del segundo producto: ")
precio2 = float(input("Precio sin impuesto de " + producto2 + ": "))
productos = {
    producto1: precio1,
    producto2: precio2
}
print(producto)
impuesto = float(input("Ingrese el porcentaje de impuesto (%): "))
precio1_final = precio1 + (precio1 * impuesto / 100)
precio2_final = precio2 + (precio2 * impuesto / 100)
print(f"Precio final de, {producto1}, :, {precio1_final}")
print(f"Precio final de, {producto2}, :, {precio2_final}")
#-----------------------------------------ejercicio 16--------------------------------------------
edad1=int(input("Edad 1: "))
edad2=int(input("Edad 2: "))
edad3=int(input("Edad 3: "))
edad4=int(input("Edad 4: "))
mayores=0
menores=0
if edad1>=18:
    mayores+=1
else:
    menores+=1

if edad2>=18:
    mayores+=1
else:
    menores+=1

if edad3>=18:
    mayores+=1
else:
    menores+=1

if edad4>=18:
    mayores+=1
else:
    menores+=1
print(f"Mayores de edad:, {mayores}")
print(f"Menores de edad:, {menores}")
#-----------------------------------------ejercicio 17--------------------------------------------
dolares=float(input("Ingrese la cantidad en dólares: "))
tasa_euro=0.85
tasa_peso=4000
tasa_yen=145
euros=dolares*tasa_euro
pesos=dolares*tasa_peso
yenes=dolares*tasa_yen
conversiones = (euros, pesos, yenes)
print(f"Conversiones en euros,pesos y yenes:, {conversiones}")
#-----------------------------------------ejercicio 18--------------------------------------------
nombre1=input("Nombre del primer producto: ")
cantidad1=int(input("Cantidad vendida de " + nombre1 + ": "))
nombre2=input("Nombre del segundo producto: ")
cantidad2=int(input("Cantidad vendida de " + nombre2 + ": "))
nombre3=input("Nombre del tercer producto: ")
cantidad3=int(input("Cantidad vendida de " + nombre3 + ": "))
ventas={
    nombre1: cantidad1,
    nombre2: cantidad2,
    nombre3: cantidad3
}
print(ventas)
total=cantidad1 + cantidad2 + cantidad3
print(f"Total de unidades vendidas:, {total}")
#-----------------------------------------ejercicio 19--------------------------------------------
t1=float(input("Temperatura 1: "))
t2=float(input("Temperatura 2: "))
t3=float(input("Temperatura 3: "))
t4=float(input("Temperatura 4: "))
t5=float(input("Temperatura 5: "))
t6=float(input("Temperatura 6: "))
t7=float(input("Temperatura 7: "))
t8=float(input("Temperatura 8: "))
t9=float(input("Temperatura 9: "))
t10=float(input("Temperatura 10: "))
temperaturas=[t1, t2, t3, t4, t5, t6, t7, t8, t9, t10]
mayores_30=len([t for t in temperaturas if t > 30])
menores_10=len([t for t in temperaturas if t < 10])
print(f"Temperaturas ingresadas:, {temperaturas}")
print(f"Cantidad mayores a 30°:, {mayores_30}")
print(f"Cantidad menores a 10°:, {menores_10}")
#-----------------------------------------ejercicio 20--------------------------------------------
p1=float(input("Ingrese el primer precio: "))
p2=float(input("Ingrese el segundo precio: "))
p3=float(input("Ingrese el tercer precio: "))
p4=float(input("Ingrese el cuarto precio: "))
p5=float(input("Ingrese el quinto precio: "))
precios=[p1, p2, p3, p4, p5]
print("Lista original:", precios)
eliminar=float(input("Escribe el precio que quieres eliminar: "))
if eliminar in precios:
    precios.remove(eliminar)
else:
       print("Ese precio no está en la lista.")
agregar = float(input("Escribe un nuevo precio para agregar: "))
precios.append(agregar)
precios.sort()
print(f"Lista actualizada y ordenada:, {precios}")