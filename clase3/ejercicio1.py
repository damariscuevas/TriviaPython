# Ejercicio 1: Contador de Números Específicos 
# Escribe un programa que cuente cuántas veces 
# aparece un número específico en una lista.

lista_denumeros = [1, 2, 3, 4, 5]
numero_usuario = int(input("Ingrese el número a buscar: "))
numero_enlalista = lista_denumeros.count(numero_usuario)

print("Lista de números: ", lista_denumeros)
print("Ingrese el número a buscar: ", numero_usuario)
print("El número", numero_usuario, " aparece ", numero_enlalista, "veces en la lista")

