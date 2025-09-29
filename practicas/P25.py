IVA = 16 / 100
# calcular el iva
def calcIVA(precio):
    return precio * IVA

# calcular cantidad + iva
def calcTotal(precio):
    iva = calcIVA(precio)
    return round(precio + iva, 2)

precio = float(input('Precio origial: '))
print(calcTotal(precio))
