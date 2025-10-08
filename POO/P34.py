AGREGAR = '1'
ACTUALIZAR = '2'
ELIMINAR = '3'
MOSTRAR = '4'
BUSCAR = '5'
SALIR = 's'

class Libro:
    nombre=''
    disponible=True
    def nombrar(self, nombre: str):
        self.nombre = nombre
        return self
    def disponibilizar(self):
        self.disponible = True
        return self
    def ocupar(self):
        self.disponible = False
        return self
    def cambiarDispo(self):
        self.disponible = not self.disponible
        return self

def mostrar_menu():
    longitud = 126
    msg = ' Que accion quieres hacer? '
    longitud_antes = 2

    # Calcula la longitud del espacio faltante
    longitud_despues = longitud - len(msg) - longitud_antes

    print('+' + ('-' * longitud_antes) + msg + ('-' * longitud_despues)+'+')
    print('|' + (' ' * 126) + '|')
    print('|', end='    ')
    print('(' + AGREGAR + ') Agregar libro', end='    ')
    print('(' + ACTUALIZAR + ') Actualizar libro', end='    ')
    print('(' + ELIMINAR + ') Eliminar libro', end='    ')
    print('(' + MOSTRAR + ') Mostrar libros', end='    ')
    print('(' + BUSCAR + ') Buscar libro', end='    ')
    print('(' + SALIR + ') Salir', end='    ')
    print('|')
    print('|' + (' ' * 126) + '|')
    print('+' + ('-' * 126) + '+')
    return input()

def ajustar(palabra: str, longitud: int, es_index: bool = False):
    if es_index:
        return (' ' * (longitud - len(palabra))) + palabra
    return palabra + (' ' * (longitud - len(palabra)))

def mostrar_libros(libros: list[Libro]):
    DISPONIBLE = 'disponible'
    NO_DISPONIBLE = 'ocupado'

    longitud = len(libros)

    indice_col = 'Indice'
    nombre_col = 'Nombre'
    info_col = 'Estado'

    index_longitud = len(indice_col)
    info_longitud = len(DISPONIBLE)
    nombre_longitud = 0
    
    if len(str(longitud - 1)) > index_longitud: index_longitud = len(str(longitud - 1))

    for libro in libros:
        if libro.nombre == '': continue # Para reutilizar funcion en "Buscar libro"
        if len(libro.nombre) > nombre_longitud: nombre_longitud = len(libro.nombre)

    print('+-' + '-' * index_longitud, '-' * nombre_longitud, '-' * info_longitud, sep='-+-', end='-+\n')
    print('| ' + ajustar(indice_col, index_longitud), ajustar(nombre_col, nombre_longitud), ajustar(info_col, info_longitud), '', sep=' | ')
    for index in range(longitud):
        libro = libros[index]
        if libro.nombre == '': continue # Para reutilizar funcion en "Buscar libro"
        str_index = str(index)
        if libro.disponible: info = DISPONIBLE
        else: info = NO_DISPONIBLE

        print('| ' + ajustar(str_index, index_longitud, True), ajustar(libro.nombre, nombre_longitud), ajustar(info, info_longitud), '', sep=' | ')
    
    print('+-' + '-' * index_longitud, '-' * nombre_longitud, '-' * info_longitud, sep='-+-', end='-+\n')
        

def buscar_libros(nombre: str):
    libros: list[tuple[int, Libro]] = []
    for i in range(len(biblioteca)):
        libro = biblioteca[i]
        if nombre.lower() in libro.nombre.lower():
            libros.append((i,libro))
    return libros

biblioteca: list[Libro] = [Libro().nombrar('El principito'), Libro().nombrar('Cenicienta').ocupar()]

while True:
    accion = mostrar_menu()
    if accion == SALIR: break
    elif accion == AGREGAR:
        nombre = input('Nombre del libro a agregar: ')
        if len(buscar_libros(nombre)) == 0:
            biblioteca.append(Libro().nombrar(nombre))
        else: print("El libro '" + nombre + "' ya existe")
    elif accion == ACTUALIZAR:
        nombre = input('Nombre del libro a actualizar: ')
        libros = buscar_libros(nombre)
        if len(libros) == 0: print("El libro '" + nombre + "' no existe")
        elif len(libros) > 1: print("Hay mas de un libro que coincide con '", nombre, "'", sep='')
        else:
            (index, libro), = libros
            biblioteca[index] = libro.cambiarDispo()
    elif accion == ELIMINAR:
        nombre = input('Nombre del libro a eliminar: ')
        libros = buscar_libros(nombre)
        if len(libros) == 0: print("El libro '" + nombre + "' no existe")
        elif len(libros) > 1: print("Hay mas de un libro que coincide con '", nombre, "'", sep='')
        else:
            (index, libro) = libros[0]
            confirmar = input("¿Estás seguro que deseas eliminar '" + libro.nombre + "'? (s/n): ")
            if confirmar.lower() == 's':
                del biblioteca[index]
    elif accion == MOSTRAR: mostrar_libros(biblioteca)
    elif accion == BUSCAR:
        nombre = input('Nombre del libro a buscar: ')
        libros = buscar_libros(nombre)
        if len(libros) != 0:
            libros_mostrar = [Libro() for _ in range(len(biblioteca))]
            for (index, libro) in libros:
                libros_mostrar[index].nombrar(libro.nombre)
            mostrar_libros(libros_mostrar)
        else: print("No se encontro el libro '" + nombre + "'")
    else:
        print("'" + accion + "' no es una accion valida")
    print()
