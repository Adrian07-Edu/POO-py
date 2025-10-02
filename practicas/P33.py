# 6 elementos {}
# buscar precio - imprimir
# buscar palabra color (no existe) - imprimir
# modificar un valor - imprimir
# agregar un nuevo key-value - imprimir
# eliminar un valor - imprimir

def print_producto():
    global producto
    tamaño_clave = 0
    tamaño_valor = 0
    for clave, valor in producto.items():
        tamaño_c = len(clave)
        if tamaño_c > tamaño_clave: tamaño_clave = tamaño_c
        tamaño_v = len(str(valor))
        if tamaño_v > tamaño_valor: tamaño_valor = tamaño_v
    
    print('', '-' * (tamaño_clave+2), '-' * (tamaño_valor+2), '', sep='+')

    for clave, valor in producto.items():
        print('| ',clave, ' ' * (tamaño_clave - len(clave)), sep='',end=' ')
        print('| ',valor, ' ' * (tamaño_valor - len(str(valor))), sep='',end=' ')
        print('|')

    print('', '-' * (tamaño_clave+2), '-' * (tamaño_valor+2), '', sep='+')

def print_clave(clave):
    global producto
    if clave in producto:
        print("'"+clave+"'", '=', producto[clave])
    else:
        print('No existe la clave:', clave)

producto = {'nombre': 'candado', 'descripcion': 'mantiene seguro', 'marca': 'good lock', 'precio': 25.99, 'material': 'acero inoxidable', 'unidades': 4}
print_producto()
print_clave('precio')
print_clave('color')

producto['unidades'] = 2
print_producto()
producto['tamaño'] = '4cm'
print_producto()
del producto['descripcion']
print_producto()
