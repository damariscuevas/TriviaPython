# Ejercicio 2: Suma de Sublistas 
#Crea un programa que tome una lista de números y 
# calcule la suma de una sublista especificada por el usuario.

mi_lista = [10, 20, 30, 40, 50, 60]
indice_inicio = int(input("Ingrese el índice de inicio de la sublista: "))
indice_final = int(input("Ingrese el índice final de la sublista: "))
sublista = mi_lista[indice_inicio:indice_final]
suma_sublista = sum(sublista)

print("Lista de números: ", mi_lista)
print("Ingrese el índice de inicio de la sublista: ", indice_inicio)
print("La suma de la sublista es: ", suma_sublista)


