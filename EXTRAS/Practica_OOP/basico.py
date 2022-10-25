class Alumnos:
    def __init__(self, nombre, apellido, curso):
        self.nombre = nombre
        self.apellido = apellido
        self.curso = curso
        self.materias = []

alumno001 = Alumnos("Lucia","Granados","2")
alumno001.materias.append("ingles")
print(alumno001.nombre,alumno001.apellido,alumno001.materias)
alumno001.materias.remove("ingles")
print(alumno001.nombre,alumno001.apellido,alumno001.materias)
alumno002 = Alumnos("Marcos","Granados","3")
alumno002.materias.append("matematica")
print(alumno002.nombre,alumno002.apellido,alumno002.materias)