
# codigo, nombre, precio, stock

class Producto:
    def __init__(self, codigo: str, nombre: str, precio: float, stock: int):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    def mostrar(self):
        precio_r = round(self.precio, 2)
        total_r = round(self.precio * self.stock, 2)
        print(f'{self.nombre} {self.codigo} ${precio_r} x{self.stock} (${total_r})')
    def actualizar(self, precio_str: str, stock_str: str):
        error = False
        if precio_str != '':
            try: self.precio = float(precio_str)
            except ValueError:
                print(f'El precio "{precio_str}" debe ser flotante')
                error = True
        if stock_str != '':
            error = False # Por si el dato se actualiza con exito
            try: self.stock = int(stock_str)
            except ValueError:
                print(f'El precio "{stock_str}" debe ser entero')
                error = True

        if not error:
            print('Actualizado con exito')

def agregar_producto():
    codigo = input('>> Ingresa el codigo del producto: ')
    nombre = input('>> Ingresa el nombre del producto: ')
    try: precio = float(input('>> Ingresa el precio del producto: '))
    except ValueError:
        print('El precio debe ser flotante')
        return 
    try: stock = int(input('>> Ingresa el stock del producto: '))
    except ValueError:
        print('El stock debe ser entero')
        return

    producto = Producto(codigo, nombre, precio, stock)
    producto.mostrar()
    inventario.append(producto)
def mostrar_inventario():
    for producto in inventario: producto.mostrar()
def buscar_producto():
    identificador = input('>> Ingresa el nombre o codigo del producto: ')
    for producto in inventario:
        if producto.nombre == identificador or producto.codigo == identificador:
            producto.mostrar()
            break
    else: print('Producto no encontrado')
    
def actualizar_producto():
    identificador = input('>> Ingresa el nombre o codigo del producto: ')
    for producto in inventario:
        if producto.nombre == identificador or producto.codigo == identificador:
            precio = input('>>> Ingresa el nuevo precio: ')
            stock = input('>>> Ingresa el nuevo stock: ')
            producto.actualizar(precio, stock)
            break
    else: print('Producto no encontrado')
def eliminar_producto():
    identificador = input('>> Ingresa el nombre o codigo del producto: ')
    for i in range(len(inventario)):
        producto = inventario[i]
        if producto.nombre == identificador or producto.codigo == identificador:
            del inventario[i]
            print(f'"{identificador}" eliminado con exito')
            break
    else: print('Producto no encontrado')
    
inventario: list[Producto] = []
while True:
    print('+- Menu de inventario ------+')
    print('| 1.- Agregar producto      |')
    print('| 2.- Mostrar inveentario   |')
    print('| 3.- Buscar producto       |')
    print('| 4.- Actualizar producto   |')
    print('| 5.- Eliminar producto     |')
    print('| 6.- Salir                 |')
    print('+---------------------------+')

    opcion = input('> Selecciona una opcion: ')
    if opcion == '1':
        agregar_producto()
    elif opcion == '2':
        mostrar_inventario()
    elif opcion == '3':
        buscar_producto()
    elif opcion == '4':
        actualizar_producto()
    elif opcion == '5':
        eliminar_producto()
    elif opcion == '6':
        print('Saliendo del sistema')
        break
    else:
        print(f'"{opcion}" no es una opcion valida')
    print()
