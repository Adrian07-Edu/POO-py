# agregar libr
# actualizar
# eliminar
# mostrar
# buscar
# salir
AGREGAR = '1'
ACTUALIZAR = '2'
ELIMINAR = '3'
MOSTRAR = '4'
BUSCAR = '5'
SALIR = 's'

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

def ajustar(palabra, longitud, es_index=False):
    if es_index:
        return (' ' * (longitud - len(palabra))) + palabra
    return palabra + (' ' * (longitud - len(palabra)))

def mostrar_libros():
    DISPONIBLE = 'disponible'
    NO_DISPONIBLE = 'ocupado'
    
    global biblioteca
    longitud = len(biblioteca)

    indice_col = 'Indice'
    nombre_col = 'Nombre'
    info_col = 'Estado'

    index_longitud = len(indice_col)
    info_longitud = len(DISPONIBLE)
    nombre_longitud = 0
    
    if len(str(longitud - 1)) > index_longitud: index_longitud = len(str(longitud - 1))

    for libro in biblioteca:
        if len(libro['nombre']) > nombre_longitud: nombre_longitud = len(libro['nombre'])

    print('+-' + '-' * index_longitud, '-' * nombre_longitud, '-' * info_longitud, sep='-+-', end='-+\n')
    print('| ' + ajustar(indice_col, index_longitud), ajustar(nombre_col, nombre_longitud), ajustar(info_col, info_longitud), '', sep=' | ')
    for index in range(longitud):
        libro = biblioteca[index]
        str_index = str(index)
        if libro['disponible']: info = DISPONIBLE
        else: info = NO_DISPONIBLE

        print('| ' + ajustar(str_index, index_longitud, True), ajustar(libro['nombre'], nombre_longitud), ajustar(info, info_longitud), '', sep=' | ')
    
    print('+-' + '-' * index_longitud, '-' * nombre_longitud, '-' * info_longitud, sep='-+-', end='-+\n')
        

def buscar_libro(nombre):
    global biblioteca
    for i in range(len(biblioteca)):
        libro = biblioteca[i]
        if libro['nombre'].lower() == nombre.lower():
            return (i,libro)
    return (-1,)

biblioteca = [{'nombre': 'El principito', 'disponible': True}, {'nombre': 'Cenicienta', 'disponible': False}]

while True:
    accion = mostrar_menu()
    if accion == SALIR: break
    elif accion == AGREGAR:
        nombre = input('Nombre del libro a agregar: ')
        if buscar_libro(nombre) == (-1,):
            biblioteca.append({'nombre': nombre, 'disponible': True})
        else: print("El libro '" + nombre + "' ya existe")
    elif accion == ACTUALIZAR:
        nombre = input('Nombre del libro a actualizar: ')
        index, libro = buscar_libro(nombre)
        if index == -1:
            print("El libro '" + nombre + "' no existe")
        else: biblioteca.append({'nombre': nombre, 'disponible': not libro['disponible']})
    elif accion == ELIMINAR:
        nombre = input('Nombre del libro a eliminar: ')
        index, _ = buscar_libro(nombre)
        if index == -1:
            del biblioteca[index]
        else: print("El libro '" + nombre + "' no existe")
    elif accion == MOSTRAR: mostrar_libros()
    elif accion == BUSCAR:
        nombre = input('Nombre del libro a buscar: ')
        index, libro = buscar_libro(nombre)
        if index != -1:
            print(libro_a_str(libro))
        else: print("No se encontro el libro '" + nombre + "'")
    else:
        print("'" + accion + "' no es una accion valida")
    print()
