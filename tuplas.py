"""#--------------------------------tupla a lsita---------------------------------------------------------
mi_tupla=(1,2,3)
mi_lista=list(mi_tupla)
print(mi_lista)
#--------------------------------lista a tupla---------------------------------------------------------
mi_lista=(4,5,6)
mi_tupla=tuple(mi_lista)
print(mi_tupla)
#--------------------------------ejercicio 1 lista de frutas---------------------------------------------------------
tupla=("manzana","pera")
lista=list(tupla)
print(lista)
fruta_nueva=input("escribre una fruta: ")
lista.append(fruta_nueva)
fruta_final=tuple(lista) 
print(f"tupla de las frutas {fruta_final}")
#--------------------------------ejercicio 2 calificaciones de un estudiante---------------------------------------------------------
tupla2=(4.2, 3.8)
lista2=list(tupla2)
print(lista2)
nueva_nota=float(input("escribre una nueva nota: "))
lista2.append(nueva_nota)
notas=tuple(lista2)
print(f"las notas del estudiantes son {notas}")
#--------------------------------ejercicio 3 datos personales ---------------------------------------------------------
tupla3=("Ana","Gomez")
lista3=list(tupla3)
print(lista3)
numero_documento=input("ingresa tu numero de documento: ")
lista3.append(numero_documento)
nombre=tuple(lista3)
print(f"Datos completos: {nombre}")"""
#--------------------------------------EJERCICIOS PRACTICOS------------------------------------
#---------------------------------------EJERCICIO 1---------------------------------------------
tupla=(1,2,3,4,5)
print(f"esta es una tupla de numeros {tupla}")
#---------------------------------------Ejercicio 2---------------------------------------------
print(f"el segundo valor es {tupla[1]}")
#---------------------------------------EJERCICIO 3---------------------------------------------
tupla=(1,2,3,4,5)
print(f"la tupla tiene {len(tupla)} elementos")
#---------------------------------------EJERCICIO 4---------------------------------------------
print(f"el numero 4 se encuentra en la posicion {tupla.index(4)}")
#---------------------------------------EJERCICIO 5---------------------------------------------
print(f"el numero 2 aparece {tupla.count(2)} vez")
#---------------------------------------EJERCICIO 6---------------------------------------------
tupla2=("una cadena de texto",40,3.5)
print(f"tupla con tipos mezclados {tupla2}")
#---------------------------------------EJERCICIO 7---------------------------------------------
#crea un tupla que contiene otra tupla
tupla_anidada=((100,500),"inicio")
#acceder al primer valor de la tupla interna
primer_valor_externo=tupla_anidada[0][0]
#mostrar el resultado
print(f"primer valor de la tupla interna: {primer_valor_externo}")









