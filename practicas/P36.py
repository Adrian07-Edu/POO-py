class Persona:
    nombre = 'Juan'
    apellido = 'Juarez'

    def saludar(self):
        print('Hola, soy {} {}'.format(self.nombre, self.apellido))

juan = Persona()
juan.saludar()