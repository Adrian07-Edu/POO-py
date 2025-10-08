class Telefono:
    marca = "Huawei"
    color = "Negro"
    ram = 32
    rom = 128
    modelo = "45GH"
    def llamar(self, mensaje: str):
        return mensaje
    def escucharMusica(self):
        print("Estas escuchando musica")
    def __str__(self) -> str:
        return \
        f'- Caracteristicas -\n' \
        f'  Marca: {self.marca}\n' \
        f'  Color: {self.color}\n' \
        f'  Ram: {self.ram}\n' \
        f'  Rom: {self.rom}\n' \
        f'  Modelo: {self.modelo}\n' \
        f'-------------------'

celular = Telefono()
print(celular)
print(celular.llamar("Hola, ¿con quien hablo?"))
celular.escucharMusica()
