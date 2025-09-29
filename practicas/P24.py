def cuadrados(lista):
    lista_cuadrados = []
    for numero in lista:
        lista_cuadrados.append(numero ** 2)
    return lista_cuadrados

lista = []
for i in range(10):
    numero = int(input('Ingresa un numero [' + str(i + 1) + '/10]: '))
    lista.append(numero)

resultado = cuadrados(lista)
print(resultado)