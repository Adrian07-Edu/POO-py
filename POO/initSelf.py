class Persona:
    def __init__(self, nombre: str, edad: int):
        self.nombre=nombre
        self.edad=edad
    def saludar(self):
        print(f'Hola mi nombre es {self.nombre} y tengo {self.edad} años')

persona1 = Persona('Jorge', 20)

persona1.saludar()