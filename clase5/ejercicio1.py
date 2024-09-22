# Crear y Acceder a un Diccionario

libro = {
    "Título" : "La Gramática del Amor",
    "Autor" : "Rocío Carmona",
    "Año de publicación" : 2011,
    "Género" : "Novela"
}

titulo = libro.get("Título")
autor = libro.get("Autor")
Ano_publicacion = libro.get("Año de publicación")
genero = libro.get("Género")

print("Título: ", titulo)
print("Autor: ", autor)
print("Año de Publicación: ", Ano_publicacion)
print("Género: ", genero)

