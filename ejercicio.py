texto="Hamas gano combinando una fuerte resistencia contra la ocupacion militar con la creacion de organizaciones sociales de base y de servicio a los pobres, una plataforma y una practica que probablemente haria ganar votos en cualquier lugar. La victoria electoral de Hamas es ominosa pero comprensible, a la luz de los acontecimientos. Es enteramente justo describir a Hamas como fundamentalista, extremista y violentista, y como una seria amenaza a la paz y a un acuerdo politicamente justo. Sin embargo, es útil recordar que en aspectos importantes, Hamas no es tan extremista como otros. Por ejemplo, declara que estaría de acuerdo con una tregua con Israel sobre la base de la frontera reconocida a nivel internacional antes de la guerra arabe-israeli de junio de l967. .."
buscar=texto.find("Hamas")
buscar2=texto.find("l967")
extraer=texto[0:768]
print(buscar)
print(buscar2)
print(extraer)
#--------------------------------------------------EJERCICIO 2----------------------
texto2="Doña Uzeada de Ribera Maldonado de Bracamonte y Anaya era baja, rechoncha, abigotada. Ya no existia razon para llamar talle al suyo. Sus colores vivos, sanos, podian mas que el albayalde y el soliman del afeite, con que se blanqueaba por simular melancolias. Gastaba dos parches oscuros, adheridos a las sienes y que fingian medicamentos. Tenia los ojitos ratoniles, maliciosos. Sabia dilatarlos duramente o desmayarlos con recato o levantarlos con disimulo. Caminaba contoneando las imposibles caderas y era dificil, al verla, no asociar su estampa achaparrada con la de ciertos palmipedos domesticos. Sortijas celestes y azules le ahorcaban las falanges"
buscar2=texto2.find("simular")
buscar3=texto2.find("falanges")
extraer=texto2[238:655]
print(buscar2)
print(buscar3)
print(extraer)
#-------------------------------------------------EJERCICIO 3-------------------------
texto3="En el texto argumentativo, el autor plantea una hipotesis o toma una posicion frente a un determinado tema (como en este caso frente a la politica de Bush) y la mantiene a lo largo del texto, reforzando su opinion por medio del desarrollo de sus ideas, ejemplos, etc. Mediante la argumentacion, el emisor pretende influir sobre su destinatario y lograr la aprobacion y/o adhesion del receptor a la idea que postula. Este tipo de textos tienen tambien como caracteristica un caracter dialogico: un dialogo con el pensamiento del otro para transformar su opinion."
buscar3=texto3.find("En")
buscar4=texto3.find("opinion.")
extraer2=texto3[0:561]
print(buscar3)
print(buscar4)
print(extraer2)
#-------------------------------------------------EJERCICIO 4-------------------------
texto4="Los flamencos son aves gregarias altamente especializadas, que habitan sistemas salinos de donde obtienen su alimento (compuesto generalmente de algas microscópicas e invertebrados) y materiales para desarrollar sus hábitos reproductivos."
buscar4=texto4.find("Los")
buscar5=texto4.find("reproductivos.")
extraer3=texto4[0:238]
print(buscar4)
print(buscar5)
print(extraer3)
#---------------------------------------------------EJERCICIO 5--------------------------
equipo=input("ingresa el nombre del equipo de futbol: ")
puntos1=int(input("ingresa los puntos del equipos 1: "))
puntos2=int(input("ingresa los puntos del equipos 2: "))
puntos3=int(input("ingresa los puntos del equipos 3: "))
puntos4=int(input("ingresa los puntos del equipos 4: "))
puntos5=int(input("ingresa los puntos del equipos 5: "))
suma=puntos1+puntos2+puntos3+puntos4+puntos5
resul2=suma//5
print(f"el promedio final de puntos es: {resul2} del equipo {equipo}")
#---------------------------------------------------EJERCICIO 6--------------------------
variable1="python es un "
variable2="lenguaje de "
variable3="progamacion "
variable4="versatil"
print(f"Objetivo: {variable1}{variable2}{variable3}{variable4}")
#---------------------------------EJERCICIO LISTA------------------------------------------
#-----------------------------------EJERCICIO 1------------------------------------------
frutas=[]
print(frutas)
fruta1=input("Escribre 1 fruta: ")
frutas.append(fruta1)
fruta2=input("Escribre otra fruta: ")
frutas.append(fruta2)
fruta3=input("Escribre otra fruta: ")
frutas.append(fruta3)
frutas.append("mora")
print(frutas)
#-----------------------------------EJERCICIO 2------------------------------------------
edades=[]
print(edades)
edad1=int(input("Escribre una edad: "))
edades.append(edad1)
edad2=int(input("Escribre otra edad: "))
edades.append(edad2)
print(edades)
#-----------------------------------EJERCICIO 3------------------------------------------
notas=[]
print(notas)
nota1=float(input("Escribre una nota con decimales: "))
notas.append(nota1)
nota2=float(input("Escribre otra nota con decimales: "))
notas.append(nota2)
print(notas)
suma=nota1+nota2
promedio=suma/2
print(f"el promedio de las notas es {promedio}")
#-------------------------------------------------Ejercicio 4-----------------------------------------------
productos=[]
produc1=input("Ingresa el primer producto: ")
produc2=input("Ingresa el segundo producto: ")
produc3=input("Ingresa el tercer producto: ")
productos.append(produc1)
productos.append(produc2)
productos.append(produc3)
print("Lista de productos:", productos)
#-------------------------------------------------Ejercicio 5-----------------------------------------------
precio1=float(input("Ingresa el precio del primer artículo: "))
precio2=float(input("Ingresa el precio del segundo artículo: "))
precio3=float(input("Ingresa el precio del tercer artículo: "))
precios=[]
precios.append(precio1)
precios.append(precio2)
precios.append(precio3)
suma_total=precio1+precio2+precio3
print("Suma total de los precios:", suma_total)
#-------------------------------------------------Ejercicio 6-----------------------------------------------
num1=int(input("Ingresa el primer número: "))
num2=int(input("Ingresa el segundo número: "))
num3=int(input("Ingresa el tercer número: "))
num4=int(input("Ingresa el cuarto número: "))
numeros=[]
numeros.append(num1)
numeros.append(num2)
numeros.append(num3)
numeros.append(num4)
mayor=max(numeros)
menor=min(numeros)
print("Números ingresados:", numeros)
print("Mayor número:", mayor)
print("Menor número:", menor)






