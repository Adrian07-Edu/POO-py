# Forma corta - (No sigue las especificaciones del problema). Utiliza el operador 'in' y 'not'
# for letra in palabra:
#     if not letra in "AEIOU":
#         print(letra)

palabra = input("Introduce una palabra: ").upper()
for letra in palabra:
    if letra == "A": continue
    elif letra == "E": continue
    elif letra == "I": continue
    elif letra == "O": continue
    elif letra == "U": continue
    else: print(letra)

print()
