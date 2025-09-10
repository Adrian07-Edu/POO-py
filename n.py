from random import randint

secret_number = randint(1, 100)
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
tries = 1 
while selected_number != secret_number:
    if selected_number < secret_number:
        print("¡Ja, ja! ¡Estás atrapado en mi bucle! El número es mayor.")
    else:
        print("¡Ja, ja! ¡Estás atrapado en mi bucle! El número es menor.")
    selected_number = int(input("Introduce un número: "))
    tries += 1
print("¡Bien hecho, muggle! Eres libre ahora. Intentos:", tries)
