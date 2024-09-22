# Crear un diccionario
persona = {
    "nombre" : "Alejandra",
    "edad" : 30,
    "ciudad" : "Mérida"
}

# Usamos el método Items
pares_clave_valor = persona.items()

# Imprimimos
print("Pares clave valor: ", pares_clave_valor)

# Convertir a una clave valor como lista
valores_lista = list(pares_clave_valor)
print("Valores como lista: ", valores_lista)