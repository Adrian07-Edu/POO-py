numbers = []
for i in range(10):
    number = int(input("Agrega un valor ["+str(i+1)+"/10] "))
    numbers.append(number)
suma = 0
for n in numbers:
    suma += n
print("El suma de los numeros es:", suma)
