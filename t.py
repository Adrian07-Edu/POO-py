class Veterinaria:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.mascotas: dict[str, tuple[str, int, str]] = {}
    def registrar_mascota(self, nombre: str, tipo: str, edad: int, dueño: str):
        self.mascotas[nombre] = tipo, edad, dueño
    def mostrar_mascotas(self):
        for n, t, e, d in self.mascotas.items():
        #for n, (t, e, d) in self.mascotas.items():
            print(f'El nombre del {t} es {n}, su edad es  de {e} años y su dueño es {d}')
    def buscar_mascota(self, nombre: str):
        if nombre in self.mascotas:
            mascota = self.mascotas[nombre]
            tipo, edad, dueño = mascota
            print(f'Tipo: {tipo}')
            print(f'Edad: {edad}')
            print(f'Dueño: {dueño}')
        else:
            print(f'La mascota "{nombre}" no esta')
    def eliminar_mascota(self, i: str):
        if i in self.mascotas:
            del self.mascotas[i]
        else:
            print(f'{i} no esta en la lista')