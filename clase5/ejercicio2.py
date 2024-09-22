libro = {
    "Título" : "La Gramática del Amor",
    "Autor" : "Rocío Carmona",
    "Año de publicación" : 2011,
    "Género" : "Novela"
}

print("Diccionario de libro original: ", libro)

libro["Año de publicación"] = 1968

print("Diccionario de libro con fecha actualizada: ", libro)

del libro["Género"]

print("Diccionario de libro sin género: ", libro)
