# Manipulación de Tuplas y Comprobración de índices
frutas = "manzana", "banana", "cereza"
indice_fruta = frutas.index("banana")
print(f"La posición de la fruta banana es: ", indice_fruta)

fruta1 = "naranja"

if fruta1 in frutas:
    print("La fruta ", fruta1, "está en la tupla.")
else:
    print("La fruta", fruta1, "no está en la tupla.")
    

