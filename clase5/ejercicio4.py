lista_estudiantes = [
    {"Nombre" : "Alma Rivas", "Edad" : 29, "Calificaciones" : [100, 95, 82]},
    {"Nombre" : "Cristina Peralta", "Edad" : 28, "Calificaciones" : [90, 87, 94]},
    {"Nombre" : "Carolina Castro", "Edad" : 31, "Calificaciones" : [85, 98, 93]}
    ]
    
estudiante1 = lista_estudiantes[0]
nombre1 = estudiante1.get("Nombre")
calificaciones1 = estudiante1.get("Calificaciones")
print(f"Nombre: {nombre1}")
print(f"Calificaciones: {calificaciones1}")
