class Estudiante:
    def __init__(self, nombre: str, matricula: str, carrera: str) -> None:
        self.nombre = nombre
        self.matricula = matricula
        self.carrera = carrera
        self.calificaciones: list[float] = []


    def agregar_calificacion(self, calificacion: float):
        self.calificaciones.append(calificacion)
        print(f'La calificación {calificacion} agregada al alumno: {self.nombre}')

    def obtenerPromedio(self):
        if len(self.calificaciones) == 0: return 0
        exacto = sum(self.calificaciones) / len(self.calificaciones)
        return round(exacto, 1)

    def mostrar_info(self):
        promedio = self.obtenerPromedio()
        print(f'- Nombre: {self.nombre}, Matricula: {self.matricula}, Carrera: {self.carrera}')
        print(f'-- Calificaciones: {self.calificaciones}, Promedio: {promedio}')

registro: list[Estudiante] = []
def agregar_estudiante():
    nombre = input('>> Nombre del estudiante: ')
    matricula = input('>> Numero de matricula: ')
    carrera = input('>> Carrera: ')

    estudiante = Estudiante(nombre, matricula, carrera)
    registro.append(estudiante)
    print(f'Estudiante {nombre} registrado con exito')

def buscar_estudiante():
    matricula = input('>> Ingresa la matricula a buscar: ')
    for estudiante in registro:
        if estudiante.matricula != matricula: continue # Este no es, seguimos buscando
        estudiante.mostrar_info()
        break # Ya se encontro, dejamos de buscar
    else:
        print(f'No se encontro a nadie con la matricula {matricula}')

def mostrar_estudiantes():
    for estudiante in registro:
        estudiante.mostrar_info()

def agregar_calificacion():
    matricula = input('>> Ingresa la matricula del estudiante: ')
    for estudiante in registro:
        if estudiante.matricula != matricula: continue # Este no es, seguimos buscando
        calificacion = input('>>> Ingresa la calificacion: ')
        estudiante.agregar_calificacion(float(calificacion))
        break # Ya se encontro, dejamos de buscar
    else:
        print(f'No se encontro a nadie con la matricula {matricula}')
def eliminar_estudiante():
    matricula = input('>> Ingresa la matricula del estudiante: ')
    for i in range(len(registro)):
        estudiante = registro[i]
        if estudiante.matricula != matricula: continue # Este no es, seguimos buscando
        del registro[i]
        print('El estudiante con la matricula', estudiante.matricula, 'fue eliminado')
        break # Ya se encontro, dejamos de buscar
    else:
        print(f'No se encontro a nadie con la matricula {matricula}')

def actualizar_estudiante():
    matricula = input('>> Ingresa la matricula del estudiante: ')
    for i in range(len(registro)):
        estudiante = registro[i]
        if estudiante.matricula != matricula: continue # Este no es, seguimos buscando
        nombre = input('>>> Ingresa el nuevo nombre: ')
        carrera = input('>>> Ingresa la nueva carrera: ')

        if nombre != '': estudiante.nombre = nombre
        if carrera != '': estudiante.carrera = carrera

        print('El estudiante con la matricula', estudiante.matricula, 'fue actualizado')
        break # Ya se encontro, dejamos de buscar
    else:
        print(f'No se encontro a nadie con la matricula {matricula}')


while True:
    print('+- Menu de registro estdiantil -----+')
    print('| 1.- Agregar estudiante            |')
    print('| 2.- Mostrar estudiantes           |')
    print('| 3.- Buscar estudiante             |')
    print('| 4.- Agregar calificación          |')
    print('| 5.- Eliminar estudiante           |')
    print('| 6.- Actualizar estudiante           |')
    print('| 7.- Salir                         |')
    print('+-----------------------------------+')

    opcion = input('> Selecciona una opcion: ')
    if opcion == '1':
        agregar_estudiante()
    elif opcion == '2':
        mostrar_estudiantes()
    elif opcion == '3':
        buscar_estudiante()
    elif opcion == '4':
        agregar_calificacion()
    elif opcion == '5':
        eliminar_estudiante()
    elif opcion == '6':
        actualizar_estudiante()
    elif opcion == '7':
        print('Saliendo del sistema')
        break
    else:
        print(f'"{opcion}" no es una opcion valida')
    print()
