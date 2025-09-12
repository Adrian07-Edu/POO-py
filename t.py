i = 0
n = 0
while n != 10:
    if n < 0:
        print("Tu numero no debe ser negativo: ", n)
        break
    number = int(input("Introduce un numero: "))
    if number == 0:
        print("Tu numero actual es:", n)
        continue
    if number < 0:
        number *= -1
    if i % 2 == 0:
        number *= -1
        n += number
        i += 1
    else:
        print("Saliste del bucle")