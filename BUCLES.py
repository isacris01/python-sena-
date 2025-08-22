"""num=5
while num > 0 :
    print(f"{num}")
    num -=1
print("termino el conteo!")
#--------------------ejemplo 2-------------------
numero=int(input("ingrese un numero de la tabla de multiplicar: ")) #Pide al ususario un numero y lo convierte a entero
i=1  #inicializacion,iniciamos  el contador en 1(primer multiplicador)
print(f"/inicia el contador en 1 {numero}:") #imprime un titulo para la tabla de multiplicar
while i <= 10: #Bucle que se repite mientras i sea menor o igual a 10
    print(f"{numero}*{i}={numero*i}")#muestra la multiplicacion y su resultado
    i +=1 #incrementa i en 1 en cada iteracion para avanzar en la tabla
#--------------------ejemplo 3 BREAK-------------------
i=1
while i< 6:
    print(i)
    if i==3:
        break 
    i += 1
#--------------------ejemplo 4 BREAK-------------------
x=0
while True:
    x -=1
    print(x)
    if x==0:
        break 
print("Fin del bucle ")"""
#--------------------ejemplo 5 BREAK-------------------
chance=1
while chance <= 3:
    txt=input("Escribe SI: ")
    if txt== "SI":
        print("Ok,lo conseguste en el intento",chance)
        break
    chance +=1
else:
    print("Has agotado tus tres intentos" )
