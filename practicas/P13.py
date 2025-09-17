palabra = input("Introduce una palabra: ").upper()

# Forma corta - (No sigue las especificaciones del problema). Utiliza el operador 'not in'
# for letra in palabra:
#     if letra not in "AEIOU": print(letra)

for letra in palabra:
    if letra == "A": continue
    elif letra == "E": continue
    elif letra == "I": continue
    elif letra == "O": continue
    elif letra == "U": continue
    else: print(letra)
