secret_number = 777
print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")
selected_number = int(input("Introduce un número: "))
while selected_number != secret_number:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    selected_number = int(input("Introduce un número: "))
print("¡Bien hecho, muggle! Eres libre ahora.")