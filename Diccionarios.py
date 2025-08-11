persona={
    "nombre": "carlos",
    "edad": 30,
    "profesion": "ingeniero"
}
print(persona)
#-----------------------------------------EJEMPLO 1-----------------------------------------------------
auto={
    "marca": "Ford",
    "modelo": "mustang",
    "año":2022
}
#--------------------------------------3.acceder a valores-------------------------------------------
print(auto["modelo"])
#--------------------------------------4.MODIFICAR VALORES-------------------------------------------
auto["año"]=2023
print(auto)
#--------------------------------------5.AÑADIR NUEVOS ELEMENTOS-------------------------------------------
auto["color"]="rojo"
print(auto)
#--------------------------------------6.ELIMINAR ELEMENTOS-------------------------------------------
del auto["modelo"]
print(auto)
#----------------------------------------USANDO POP.--------------------------------------------------
auto.pop("marca")
print(auto)
#---------------------------------------1.["Clave."]---------------------------------------------------
auto={"marca":"Toyota","modelo":"Corolla"}
del auto["modelo"]
print(auto)
#-------------------------SI LA CLAVE NO EXISTE------------------------------------------
"""del auto["color"]
print(auto)"""
#---------------------------------------2.dicionario.pop("Clave.")---------------------------------------------------
#----------------------------------------EJEMPLO--------------------------------------------------
auto={"marca":"Toyota","modelo":"corolla"}
valor=auto.pop("marca")
print(valor)
print(auto)
#-----------------------------------con valor por defecto-----------------------------
color=auto.pop("color","No especificado")
print(color)