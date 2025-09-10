calificacion = int(input("Introduce la calificación (0-10): "))

if calificacion < 0:
    print("ERROR: Calificación por debajo del rango válido.")
elif calificacion > 10:
    print("ERROR: Calificación por encima del rango válido.")

# Valores validos: 0 a 10
elif calificacion < 5: # Menor que 5
    print("Necesitas estudiar")
elif calificacion <= 7: # Entre 5 y 7
    print("La libraste")
elif calificacion == 8:
    print("Puedes ser mejor")
elif calificacion == 9:
    print("Eres un estudiante notable")
elif calificacion == 10:
    print("Excelente")