lista = []
for i in range(int(input("Cuantos numeros quieres ingresar? "))):
    lista.append(int(input("Introduce un numero: ")))

lista.sort()

print("el numero mayor es:", lista[-1])
print("el numero menor es:", lista[0])
