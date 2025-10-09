class Animal:
    tipo = ''
    nombre = ''
    def saludar(self):
        print(f'Hola soy {self.tipo} y me llamo {self.nombre}')

animal = Animal()
animal.tipo = 'Perro'
animal.nombre = 'Firulais'
animal.saludar()