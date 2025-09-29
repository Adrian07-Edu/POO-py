def fib(indice):
    valores = [0,1]
    for i in range(indice-1):
        valores.append(valores[i]+valores[i+1])
    return valores[indice]

indice = int(input("Ingresa un numero: "))
resultado = fib(indice)
print("El numero", indice, "de fibonacci es:", resultado)