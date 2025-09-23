letras = []

vocales = 0
consonantes = 0

def analiza_letra(letra: str):
    global vocales, consonantes, letras

    minuscula = letra.lower()
    mayuscula = letra.upper()
    if minuscula == mayuscula:
        print("'" + letra + "' no es una letra válida.")
        return
    letras.append(letra)  
    if minuscula in "aeiou": vocales += 1
    else: consonantes += 1

while vocales + consonantes < 10:
    letra = input("Introduce una letra: ")
    if len(letra) != 1:
        for l in letra:
            if vocales + consonantes >= 10: break
            analiza_letra(l)
        continue
    analiza_letra(letra)
else:
    print("Letras introducidas:", letras)
    print("Consonantes:", consonantes)
    print("Vocales:", vocales)