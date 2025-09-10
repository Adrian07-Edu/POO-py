jornada = int(input("Introduce las horas trabajadas: "))
hora_normal = 15
hora_extra = 20

if jornada <= 48:
    salario = jornada * hora_normal
else:
    horas_extra = jornada - 48
    salario = (48 * hora_normal) + (horas_extra * hora_extra)
    print("Horas extra:", horas_extra)

print("El salario es:", salario)