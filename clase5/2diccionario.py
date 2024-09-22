# Crear un diccionario con información de una persona

persona = {
    "nombre" : "Roberto",
    "edad" : 29,
    "ciudad" : "Ensenada"
}

# Acceder a los elementos usando corchetes
nombre = persona["nombre"]
edad = persona["edad"]
ciudad = persona["ciudad"]

# Imprimir los valores
print("Nombre: ", nombre)
print("Edad: ", edad)
print("Ciudad: ", ciudad)

#Intentar acceder a una clave que no existe
#print(persona["pais"])
print(persona["edad"])