# Verificación de Elementos en una Tupla
mi_tupla = 3, 6, 9, 12, 15
numero_uno = 6
numero_dos = 7

if numero_uno in mi_tupla:
    print(f"El número {numero_uno} se encuentra en la tupla.")
else:
    #si el valor no está en la tupla, mostrar un mensaje
    print(f"El número {numero_uno} no está en la tupla")

if numero_dos in mi_tupla:
    print(f"El número {numero_dos} se encuentra en la tupla.")
else:
    #si el valor no está en la tupla, mostrar un mensaje
    print(f"El número {numero_dos} no se encuentra en la tupla")
    