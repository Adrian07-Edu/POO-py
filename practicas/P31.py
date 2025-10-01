lista = []
for i in range(6):
    numero = int(input('Ingresa un numero ['+str(i+1)+'/6]: '))
    lista.append(numero)

def contador(numero):
    global lista
    print('El numero', numero, 'aparece', lista.count(numero), 'veces en la lista')

dato = None
while dato != '':
    if dato != None: contador(int(dato))
    print(lista)
    dato = input('Que valor quieres buscar? ')