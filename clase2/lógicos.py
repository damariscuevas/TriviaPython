# Definimos distintas variables para usar en las comparaciones
a = 10
b = 5
c = 15
d = 8

# Operador AND
resultado_and = (a > b) and (c > d)
print(f"Resultado de (a > b) and (c > d): {resultado_and}")
# (a > b) es True porque 10 > 5
# (c > d) es True porque 15 > 8

# Operador OR
# Al menos una de las condiciones debe ser verdadera para que el resultado sea True 
resultado_or = (a < b) or (c > d)
print(f"Resultado de (a < b) or (c > d): {resultado_or}")
# (a < b) es False porque 10 no es menor que 5
# (c > d) es True porque 15 es mayor que 8

# Operador NOT
# El operador not invierte el valor de la expresión
resultado_not = not (a < b)
print(f"Resultado de not (a > b): {resultado_not}")
# (a < b) es False porque 10 no es menor que 5
# not False resulta en true

# Combinación dde los operadores lógicos and, or y not en una expresión
resultado_combinado =c (a > b) and (not (c > d)) or (b < c)
print(f"Resultado combinado: {resultado_combinado}")
# (a > b) es True porque 10 > 5
# (c < d) es False porque 15 no es menor que 8, y not (false) resulta en true
# (a > b) and (c < d) es True porque true and true resulta en true
# True or true resulta en true

