IVA = 16 / 100
# calcular el iva
def calcIVA(precio):
    return precio * IVA

# calcular cantidad + iva
def calcTotal(precio):
    iva = calcIVA(precio)
    return precio + iva

print(calcTotal(int(input('Precio origial: '))))