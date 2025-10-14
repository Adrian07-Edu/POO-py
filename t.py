class Veterinaria:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.mascotas: dict[str, dict[str, str]] = {}

    def registrar_mascota(self, nombre: str, tipo: str, edad: str, dueño: str):
        self.mascotas[nombre] = { 'tipo': tipo, 'edad': edad, 'dueño': dueño }
        print(f"Se agrego la mascota de nombre {nombre}, de tipo {tipo}, de edad {edad}, de dueño {dueño}.")

    def mostrar_mascotas(self):
        for nombre, mascota in self.mascotas.items():
            tipo = mascota['tipo']
            edad = mascota['edad']
            dueño = mascota['dueño']
            print(f"El nombre del {tipo} es {nombre}, su edad es de {edad} años y su dueño es {dueño}")

    def buscar_mascota(self, nombre: str):
        if nombre in self.mascotas:
            mascota = self.mascotas[nombre]
            tipo = mascota['tipo']
            edad = mascota['edad']
            dueño = mascota['dueño']
            print(f'Tipo: {tipo}')
            print(f'Edad: {edad}')
            print(f'Dueño: {dueño}')
        else:
            print(f'La mascota "{nombre}" no está.')
            
    def eliminar_mascota(self, nombre: str):
        if nombre in self.mascotas:
            del self.mascotas[nombre]
        else:
            print("No esta en la lista.")


def mostrar_menu():
    print('Opcion(1): Registrar mascota')
    print('Opcion(2): Mostrar mascota')
    print('Opcion(3): Busar mascota')
    print('Opcion(4): Eliminar mascota')
    print('Opcion(5): Salir')


print("+----------------------------------------+")
print("|                                        |")
print("|     Bienvenidos a nuestra              |")
print("|          Veterinaria                   |")
print("|                                        |")
print("+----------------------------------------+")


vet = Veterinaria('mascota')
while True:
    mostrar_menu()
    opcion = input("Selecciona una opcion: ")
    
    if opcion == "1":
        nombre = input('Introduce su nombre: ')
        tipo = input('Introduce su tipo: ')
        edad = input('Introduce su edad: ')
        dueño = input('Introduce su dueño: ')
        vet.registrar_mascota(nombre, tipo, edad, dueño)
    elif opcion == "2":
        vet.mostrar_mascotas()
    elif opcion == "3":
        nombre = input('Nombre a buscar: ')
        vet.buscar_mascota(nombre)
    elif opcion == "4":
        nombre = input('Nombre a eliminar: ')
        vet.eliminar_mascota(nombre)
    elif opcion == "5":
        print("Saliendo del programa")
        break
    else:
        print("Opción no válida, intente de nuevo.")
