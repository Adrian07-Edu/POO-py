pesos = 826
dolares = 42

# dolar en pesos
tasa_cambio = 18.63 # dolar / pesos
# pesos en dolares
tasa_cambio_inv = round(1 / tasa_cambio, 3) # peso / dolar
# 1 / (dolar / pesos) = peso / dolar

dolares_pesos = round(dolares * tasa_cambio, 2)
pesos_dolares = round(pesos / tasa_cambio, 2)

print("+-----------+-------------+-------------+")
print("|           |   Dolares   |    Pesos    |")
print("+-----------+-------------+-------------+")
print("|      Tasa |", tasa_cambio, 'US-MX |', tasa_cambio_inv, 'MX-US |')
print("|  Cantidad | US$", dolares, '     | MX$', pesos, '    |')
print("| Resultado | MX$", dolares_pesos, ' | US$', pesos_dolares, '  |')
print("+-----------+-------------+-------------+")
