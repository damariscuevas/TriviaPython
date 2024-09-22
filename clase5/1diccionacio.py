# Ejemplo de diccionario
diccionario_vacio = {}
print("Ejemplo de un diccionario vacio: ", diccionario_vacio)

# Ejemplo básico de un diccionario
persona = {
        "nombre" : "María",
        "edad" : 30,
        "casada" : False,
        "hijos" : ["Ana", "Luis"], #clave es string y valor es una lista
        "dirección" : { #clave es un string y valor es lo que viene después de los dos puntos
            "calle" : "La gran vía",
            "ciudad" : "Madrid"
        }
}

print("Ejemplo de diccionario básico: ", persona)

# Ejemplo de diccionario con valores de distintos tipos
diccionario_mixto = {
    "nombre" : "Alejandra",
    1: [2,3,4], # clave es un entero y valor es un string
    (2, 3) : "tupla como clave" # clave es una tupla y valor es un string
}

print("Ejemplo de diccionario mixto: ", diccionario_mixto)