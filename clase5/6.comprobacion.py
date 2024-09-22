# Crear un diccionario
persona = {
    "nombre" : "Juan Carlos",
    "edad" : 26,
    "ciudad" : "Caborca"
}

# Comprobar si una clave existe en el diccionario antes de acceder a su valor
clave = "edad"

if clave in persona:
    valor = persona[clave]
    print(f"El valor de ‘{clave}’ es: {valor}")
else:
    print(f"la clave ‘{clave}’ no existe en el diccionario")
    
#Intentar acceder a una clave que no existe en el diccionario antes de acceder a su valor 
clave = "pais"

if clave in persona:
    valor = persona[clave]
    print(f"El valor de ‘{clave}’ es: {valor}")
else:
    print(f"la clave ‘{clave}’ no existe en el diccionario")