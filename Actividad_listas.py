#--------------------------------------------actividad de listas----------------------------------------------
#--------------------------------------------primer paso------------------------------------------------------
LISTA1=[15,7]
LISTA2=["uno","dos","tres","cuatro"]
LISTA1.append(100)
LISTA1.append("Hola Mundo")
print("LISTA1:",LISTA1)
#--------------------------------------------segundo paso------------------------------------------------------
LISTA2.append("Hola y Adios")
LISTA2.append(300)
print("LISTA2:",LISTA2)
#--------------------------------------------tercer paso------------------------------------------------------
LISTA1.pop()       
LISTA3=LISTA1.copy()  
LISTA1=[15,7,100]           
LISTA3=[15,7,100]           
print("LISTA3:",LISTA3)
#--------------------------------------------cuarto paso------------------------------------------------------
copia2=LISTA2.copy()
copia2.pop(0)   
copia2.pop(-1)            
LISTA4=copia2   
print("LISTA4:", LISTA4)
#--------------------------------------------quinto paso------------------------------------------------------
LISTA5=LISTA4+LISTA3
print("LISTA5:", LISTA5)