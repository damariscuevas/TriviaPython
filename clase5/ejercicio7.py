# Contar Ocurrencias de Elementos en un Diccionario Anidado
Clubes = {
    "Club Pandita":
    [
        {"Jugador" : "Marina", "Edad": 3},
        {"Jugador": "Camila", "Edad": 2},
        {"Jugador": "Aylari", "Edad": 2},
        {"Jugador": "Valentina", "Edad": 3},
        {"Jugador": "Mónica", "Edad": 3}    
    ],
    
    "Club Mariposa": 
        [
            {"Jugador" : "Lorena", "Edad": 4},
            {"Jugador" : "Emma", "Edad": 4},
            {"Jugador" : "Jacqueline", "Edad": 5},
            {"Jugador" : "Grecia", "Edad": 5}
        ],
        
        "Club Ardillas":
            [
                {"Jugador" : "Renata", "Edad": 6},
                {"Jugador" : "Sofía", "Edad": 6},
                {"Jugador" : "Susset", "Edad": 7},
                {"Jugador" : "Samantha", "Edad": 7},
                {"Jugador" : "Emily", "Edad": 6},
            ]
    }

club1 = Clubes["Club Pandita"]
jugadores1 = len(club1)
print(f"El Club Pandita tiene {jugadores1} jugadores.")

club2 = Clubes["Club Mariposa"]
jugadores2 = len(club2)
print(f"El Club Mariposa tiene {jugadores2} jugadores.")

club3 = Clubes["Club Ardillas"]
jugadores3 = len(club3)
print(f"El Club Ardillas tiene {jugadores3} jugadores.")