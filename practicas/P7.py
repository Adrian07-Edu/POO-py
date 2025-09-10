primer_numero = int(input("intoduce el primer numero: "))
segundo_numero = int(input("intoduce el segundo numero: "))
tercer_numero = int(input("intoduce el tercer numero: "))
cuarto_numero = int(input("intoduce el cuarto numero: "))

if primer_numero >= segundo_numero:
    semi_mayor_1 = primer_numero
else:
    semi_mayor_1 = segundo_numero


# numero_mayor = primer_numero
# if segundo_numero > numero_mayor:
#     numero_mayor = segundo_numero
# if tercer_numero > numero_mayor:
#     numero_mayor = tercer_numero
# if cuarto_numero > numero_mayor:
#     numero_mayor = cuarto_numero

numero_mayor = max(primer_numero, segundo_numero, tercer_numero, cuarto_numero)
print("El mayor es:", numero_mayor)
