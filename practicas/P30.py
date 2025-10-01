colores = ['rojo', 'verde', 'azul']

def en_colores(color):
    global colores
    return color in colores

print(en_colores('amarillo'))