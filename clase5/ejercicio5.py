productos_tienda = [
    {"Nombre" : "Vestido rosa", "Precio" : 525, "Cantidad en Stock" : 10 },
    {"Nombre" : "Sombrero negro" , "Precio" : 891 , "Cantidad en Stock" : 5},
    {"Nombre" : "Flats corazón", "Precio" : 679, "Cantidad en Stock" : 7},
    {"Nombre" : "Cinturón AB", "Precio" : 236, "Cantidad en Stock" : 4}
] 

producto2 = productos_tienda[1]
nombre_producto2 = producto2.get("Nombre")
precio_producto2 = producto2.get("Precio")
print(f"El producto {nombre_producto2} cuesta ${precio_producto2} pesos.")