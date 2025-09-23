vocales = []
consonantes = []
len_consonantes, len_vocales = 0, 0
while len_vocales + len_consonantes < 10:
    letra = input("Introduce una letra: ")
    longitud = len(letra)
    if longitud == 0: continue
    if longitud > 1:
        print("Por favor, introduce solo una letra.")
        continue

    minuscula = letra.lower()
    mayuscula = letra.upper()
    if minuscula == mayuscula:
        print("'" + letra + "' no es una letra válida.")
        continue

    if minuscula in "aeiouáéióú":
        vocales.append(letra)
        len_vocales = len(vocales)
    else:
        consonantes.append(letra)
        len_consonantes = len(consonantes)

print("Consonantes:", consonantes, "(" + str(len_consonantes) + ")")
print("Vocales:", vocales, "(" + str(len_vocales) + ")")
