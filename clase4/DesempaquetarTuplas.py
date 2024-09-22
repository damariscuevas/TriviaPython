# Ejemplo 1: Desempaquetado básico de tuplas
# Crear una tupla con varios tipos de datos
mi_tupla = (1, "python", 3.14)
# Desempaquetar la tupla
numero, lenguaje, p1 = mi_tupla
#mostrar el valor de cada variable después del desempaquetado
print("Número: ", numero)
print("Lenguaje: ", lenguaje)
print("Valor de P1: ", p1)

# Ejemplo 2: Número de variables no coincide con el nímero de elementos
#Crear una tupla con tres elementos
mi_tupla = (1, "python", 3.14)
#intentar desempaquetar en dos variables (esto causa error)
#numero, lenguaje = mi_tupla

# Ejemplo 3: Desempaquetado con el operador *
# Crear una tupla con varios elementos
mi_tupla = (1, "python", 3.14, "Tuplas", "Desempaquetado")
# Desempaquetar la tupla con el operador * para capturar varios elementos
primer_elemento, *resto = mi_tupla
# Mostrar los resultados
print("\nPrimer Elemento: ", primer_elemento)
print("Resto de los elementos: ", resto)
