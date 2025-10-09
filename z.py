class Libro:
    def __init__(self, nombre: str, autor: str, fecha: str):
        self.nombre = nombre
        self.autor = autor
        self.fecha = fecha
    def citar(self):
        autor = self.autor
        nombre = self.nombre
        fecha = self.fecha
        return f'{autor}. ({fecha}). {nombre}.'

libro1 = Libro('El principito', 'Saint-Exupéry', 'abr. 1943')
print(libro1.citar())