calificaciones = [float(input('Ingresa un numero [' + str(i+1) + '/8]: ')) for i in range(8)]

def calcular_promedio():
    global calificaciones
    return sum(calificaciones) / len(calificaciones)

promedio = calcular_promedio()

print("Tu promedio es de:", round(promedio, 1))
