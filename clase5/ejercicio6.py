escuela = { 
    "Nombre de la Escuela" : "Mira tus estrellas",
    "Año de fundación" : 2022,
    "Materias" : [
        {
            "Materia" : "Expresión alternativa",
            "Alumnos" : [
                {"Alumno": "Viviana Márquez", "Edad": 15},
                {"Alumno": "Erika Melgoza", "Edad": 15},
                {"Alumno": "Josefina Zepeda", "Edad": 14},
            ]
        },
        {
            "Materia": "Creatividad Corporal",
            "Alumnos" : [
                {"Alumno": "Pamela Segura", "Edad": 16},
                {"Alumno": "Xiomara Vazquez", "Edad": 15},
                {"Alumno": "Pedro Mora", "Edad": 16},
            ]
        },
        {
            "Materia": "Historia del Arte",
            "Alumnos": [
                {"Alumno": "Alonso Velazquez", "Edad": 15},
                {"Alumno": "Donaldo Ruiz", "Edad": 14},
                {"Alumno": "José Jiménez", "Edad": 13},
            ]
        }
    ]
}
estudiante1 = escuela["Materias"][0]["Alumnos"][0]["Alumno"]
print(f"El nombre del primer estudiante es:", {estudiante1})