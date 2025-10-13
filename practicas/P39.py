class Biblioteca:
    def __init__(self, nombre: str):
        self.libros: dict[str, dict[str, str | int]] = {}
        self.nombre = nombre

    def agregar_libro(self, titulo: str, autor: str, fecha: int):
        self.libros[titulo] = {'autor': autor, 'fecha': fecha}

    def mostrar_libros(self):
        print(f'Libros en {self.nombre}')
        for titulo, informacion in self.libros.items():
            print(f'{informacion['autor']}. ({informacion['fecha']}). {titulo}.')

    def buscar_libro(self, titulo: str):
        print(f'Buscando {titulo}')
        if titulo in self.libros:
            informacion = self.libros[titulo]
            print(f'Autor: {informacion['autor']}')
            print(f'Fecha: {informacion['fecha']}')
        else: print(f'El libro {titulo} no esta disponible')

    def eliminar_libro(self, titulo: str):
        if titulo in self.libros:
            informacion = self.libros[titulo]
            del self.libros[titulo]
            print(f'Se elimino el libro {titulo} de {informacion['autor']}. ({informacion['fecha']})')
        else: print(f'No se pudo eliminar el libro {titulo}')

    def editar_libro(self, titulo: str, autor: str, fecha: str):
        libro = self.libros[titulo]
        if autor != '': libro['autor'] = autor
        if fecha != '': libro['fecha'] = int(fecha)
    
    def contar_libros(self):
        print(f'Hay {len(self.libros)} libros en {self.nombre}')

def mostrar_menu():
    print('************* Menu de biblioteca *************')
    print(' 0.- Salir')
    print(' 1.- Agregar Libro')
    print(' 2.- Mostrar Libro')
    print(' 3.- Buscar Libro')
    print(' 4.- Eliminar Libro')
    print(' 5.- Editar Libro')
    print(' 6.- Contar Libros')

biblioteca = Biblioteca('biblioteca central')

biblioteca.agregar_libro('El principito', 'Antoine de Saint-Exupéry', 1943)
biblioteca.agregar_libro('1984', 'George Orwell', 1949)

while True:
    mostrar_menu()
    opcion=input('Selecciona una opcion: ')
    if opcion == '0': break
    elif opcion == '1':
        titulo = input('Titulo del libro: ')
        autor = input('Autor del libro: ')
        fecha = int(input('Publicacion del libro: '))
        biblioteca.agregar_libro(titulo, autor, fecha)
    elif opcion == '2':
        biblioteca.mostrar_libros()
    elif opcion == '3':
        titulo = input('Titulo del libro: ')
        biblioteca.buscar_libro(titulo)
    elif opcion == '4':
        titulo = input('Titulo del libro: ')
        biblioteca.eliminar_libro(titulo)
    elif opcion == '5':
        titulo = input('Titulo del libro: ')
        autor = input('Autor del libro: ')
        fecha = input('Publicacion del libro: ')
        biblioteca.editar_libro(titulo, autor, fecha)
    elif opcion == '6':
        print(f'')
    else: print(f'la opcion "{opcion}" es invalida')

# biblioteca.agregar_libro('El principito', 'Antoine de Saint-Exupéry')
# biblioteca.agregar_libro('1984', 'George Orwell')
# 
# biblioteca.mostrar_libros()
# 
# biblioteca.buscar_libro('1984')
# biblioteca.buscar_libro('Don Quijote')
# 
# biblioteca.eliminar_libro('1984')
# biblioteca.mostrar_libros()