persona = {
    "nombre" : "Nacho Delicioso",
    "edad" : 27,
    "Ciudad" : "Ensenada"
}

#Usar el método .get() para acceder a los elementos
nombre = persona.get("nombre")
edad = persona.get("edad")
ciudad = persona.get("ciudad")

#Imprimir 
print("Nombre: ", nombre)
print("Edad: ", edad)
print("ciudad ", ciudad)

#Intetnar acceder a una clave que no existe usando .get()
pais = persona.get("pais")
print("Pais:", pais) #devuelve el none

#Usar get con un valor predeterminado si la clave no existe
pais_con_valor_predeterminado = persona.get("pais", "No especificado")
print("Pais (con valor predeterminado):", pais_con_valor_predeterminado)
