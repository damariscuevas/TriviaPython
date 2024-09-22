# Crear una tupla con varios valores
tupla_mixta = (1, "hola", 3.5)

# Mostrar completa la tupla
print("Tupla completa: ", tupla_mixta)

# Acceder a los elementos de la tupla por sus índices
print("Primer elemento de la tupla: ", tupla_mixta[0])
print("Segundo elemento de la tupla: ", tupla_mixta[1])
print("Tercer elemento de la tupla: ", tupla_mixta[2])

# Explicación tuplas inmutables
print("\nLas tuplas no se pueden modificar. Intentemos cambiar un elemento de la tupla")

# Ejemplo de intento de cambio que causaría error
# tupla_mixta[0] = 10

# Explicación clara de la inmutabilidad
print("Si intentamos hacer tupla_mixta[0] = 10, Python mostrará porque no se puede cambiar ningún elemento de una tupla.")

# Mostrar como si podemos "modificar" una tupla, creando una nueva
nueva_tupla = (10, "hola", 3.5)
print("Nueva tupla con el primer elemento cambiado: ", nueva_tupla)
print("Tupla original permanece sin cambios: ", tupla_mixta)
