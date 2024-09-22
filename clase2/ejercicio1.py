# Ejercicio 1: Calificación con Operador Ternario
# Escribe un programa que asigna un mensaje a una variable resultado basado en una calificación (entre 0 y 100). 
# Usa el operador ternario para asignar "Aprobado" si la calificación es mayor o igual a 60 y "Reprobado" en caso contrario.

# DATOS
# Dato de entrada: 
# -calificación 
# Dato de salida: 
# -Mensaje: "Aprobado" si la calificación es igual o mayor a 60.
# -Mensaje: "Reprobado" si la calificación es menor a 60.


# "El problema en pasos pequeños"
# 1. Solicitar al usuario una calificación (un número de entre el 0 y el 100)
# 2. Convertir el monto a tipo float para permitir cálculos con decimales.
# 3. Verficiar si la calificación es igual o mayor a 60.
#   Si la condición es positiva:
# Mostrar mensaje de "Aprobado"
#   Si la condición en negativa:
# Mostrar mensaje de reprobado.

# Ejercicio Resuelto:

# Solicita la calificación al usuario

calificación = float(input("Introduce tu calificación: "))
mensaje = (f"Aprobado" if calificación >=60 else "Reprobado")
print(mensaje)

