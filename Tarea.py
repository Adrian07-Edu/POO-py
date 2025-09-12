numero = input("Escribe un numero: ")
longitud = len(numero)
indice = 0
tiene_punto = False

while indice < longitud:
    digito = numero[indice]
    indice += 1
    if digito in "+-":
        if indice == 1: continue
        print('Tu numero no es correcto, el caracter "' + digito + '" no esta al inicio')
        break
    if digito == ".":
        if tiene_punto:
            print('Tu numero no es correcto, contiene mas de un punto "."')
            break
        tiene_punto = True
        continue
    if not digito in "0123456789":
        print('Tu numero no es correcto, contiene el caracter "' + digito + '"')
        break
else:
    print('Tu numero fue:', float(numero))

numero = input("Escribe un numero: ")
longitud = len(numero)
indice = 0

while indice < longitud:
    digito = numero[indice]
    indice += 1
    if digito not in "0123456789":
        print('Tu numero no es correcto, contiene el caracter "' + digito + '"')
        break