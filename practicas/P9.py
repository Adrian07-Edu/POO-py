color = input("Introduce un color (en minusculas): ")

valido = True
traduccion = ''

if color == 'amarillo': traduccion = 'yellow'
elif color == 'rojo': traduccion = 'red'
elif color == 'azul': traduccion = 'blue'
elif color == 'verde': traduccion = 'green'
elif color == 'blanco': traduccion = 'white'
else: valido = False

if valido: print('La traducción de', color, 'es', traduccion)
else: print('El color', color, 'no es válido')