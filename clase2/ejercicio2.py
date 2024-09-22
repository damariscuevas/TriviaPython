# Ejercicio 2: Categoría de Edad con Operadores Lógicos
# Escribe un programa que clasifique a una persona en una categoría según su edad. 
# Usa un condicional if tradicional con operadores lógicos (and, or) para las siguientes categorías:
#✓ "Niño" si la edad está entre 0 y 12 años.
#✓ "Adolescente" si la edad está entre 13 y 19 años.
#✓ "Adulto" si la edad está entre 20 y 64 años.
#✓ "Adulto Mayor" si la edad es 65 o más.

# DATOS 
    # Datos de entrada:
# Edad
    # Datos de salida:
# Mensaje: "Niño" si la edad está entre 0 y 12 años.
# Mensaje: "Adolescente" si la edad está entre 13 y 19 años.
# Mensaje: "Adulto" si la edad está entre 20 y 64 años.
# Mensaje: "Adulto Mayor" si la edad es 65 o más.

# "El problema en pasos pequeños"
# 1. Solicitar al usuario edad
# 2. Verificar en qué categoría está:
# "Niño" si la edad está entre 0 y 12 años.
# "Adolescente" si la edad está entre 13 y 19 años.
# "Adulto" si la edad está entre 20 y 64 años.
# "Adulto Mayor" si la edad es 65 o más.
# 3. Mostrar mensaje de según la categoría:
#   Niño / Adolescente / Adulto / Adulto Mayor

# EJERCICIO RESUELTO

edad = int(input("Introduce tu edad: "))

if edad <= 12:
    print("Niño")

elif edad >= 13 and edad <= 19:
    print("Adolescente")
    
elif edad >= 20 and edad <= 64:
    print("Adulto")

else:
    print("Adulto Mayor")
    