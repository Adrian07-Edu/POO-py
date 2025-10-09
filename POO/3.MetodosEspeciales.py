class Telefono:
    def __init__(self, marca: str, color: str):
        self.marca = marca
        self.color = color
    def __del__(self):
        print('objeto destruido')

telefono = Telefono('nokia', 'negro')
print(telefono)