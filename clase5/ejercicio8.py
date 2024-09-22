libreria = {
    "Nombre de la tienda" : "Más libros que estrellas",
    "Libros" : 
        [
        
        {"Título" : "Amor a medias", "Precio" : 325.89},
        {"Título" : "Locuras del emperador", "Precio" : 25.99},
        {"Título" : "Cómo crear una secta", "Precio" : 666.66},
        {"Título" : "Mi mamá me mima", "Precio": 0.99} 
    ]
}

libro2 = libreria["Libros"] [1]
libreria["Libros"][1]["Precio"] = 15.99
titulo2 = libro2.get("Título")
precio2 = libro2.get("Precio")

print(f"El libro {titulo2} ahora cuesta ${precio2} pesos.")
