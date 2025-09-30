def es_par(n):
    return n%2 == 0
lst = []

for i in range(8):
    num = int(input("ingresa un numero: "))
    lst.append(num)
for num in lst:
    if not es_par(num): continue
    print(num)
