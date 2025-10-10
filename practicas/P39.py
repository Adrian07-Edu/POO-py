class Biblioteca:
    def __init__(self, nombre: str):
        self.libros: dict[str, str] = {}
        self.nombre = nombre
    def agregar_libro(self, nombre: str, autor: str):
        self.libros[nombre] = autor
    def mostrar_libros(self):
        print(f'Libros en {self.nombre}')
        for c, v in self.libros.items(): print(f'{c}: {v}')
    def buscar_libro(self, nombre: str):
        if nombre in self.libros:
            print(f'Autor: {self.libros[nombre]}')
        else: print('No esta disponible')

biblioteca = Biblioteca('biblioteca central')
biblioteca.agregar_libro('El principito', 'Antoine de Saint-Exupéry')
biblioteca.agregar_libro('1984', 'George Orwell')
biblioteca.buscar_libro('1984')
biblioteca.buscar_libro('Don Quijote')
biblioteca.mostrar_libros()