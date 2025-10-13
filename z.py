class Mascota:
    def __init__(self, nombre: str, edad: int, dueño: str):
        self.nombre = nombre
        self.edad = edad
        self.dueño = dueño
    def tipo(self) -> str:
        raise ValueError("No esta especificado el tipo.")


class Veterinaria:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.mascotas: list[Mascota] = []
    def registrar_mascota(self, mascota: Mascota):
        self.mascotas.append(mascota)