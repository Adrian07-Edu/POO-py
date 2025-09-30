def fib(indice):
    if indice < 0:
        print('el indice no debe ser menor a 0')
        return

    if indice == 0:
        print(0)
        return 0

    print(0, 1, end=' ')
    if indice == 1: return 1

    x, y, z = 0, 1, 0
    for i in range(indice-1):
        z = x + y
        x, y = y, z
        print(z, end=' ')

    print()
    return z

fib(12)