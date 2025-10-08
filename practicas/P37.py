class Automovil:
    marca=''
    modelo= ''
    color=''
    cilindros = 0
    def datos(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Color:", self.color)
        print("Cilindros:", self.cilindros)

coche = Automovil()
coche.marca ='nissan'
coche.modelo = 'sentra'
coche.color = 'gris'
coche.cilindros = 4
coche.datos()