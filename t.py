numeros=[2,4,6,8,10,12,14,16]
print(len(numeros))
numeros[5] = 50
print(numeros)
numeros[2] = numeros[-1]
print(numeros)
del numeros[3]
print(numeros)
numeros[1] = 'Hola'
print(numeros)