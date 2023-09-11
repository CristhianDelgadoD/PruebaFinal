class Persona:
    def __init__(self, genero, titulo, nombre, apellido):
        self.genero = genero
        self.titulo = titulo
        self.nombre = nombre
        self.apellido = apellido

    def toDBCollection(self):
        return{
            'genero': self.genero,
            'titulo': self.titulo,
            'nombre': self.nombre,
            'apellido': self.apellido
        }