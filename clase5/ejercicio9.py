clase = {
    [
        {"Nombre": "Carlos", "Edad" : 3},
        {"Nombre": "Emilio", "Edad": 3} ,
        {"Nombre": "Elian", "Edad": 3},
        {"Nombre": "Jesús", "Edad": 3},
        {"Nombre": "Sameer", "Edad": 4}]
}

def edad_indice(clase, indice):
    return clase["estudiantes"][indice]["edad"]
