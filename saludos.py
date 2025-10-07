import random
def formato_aleatorio() -> str:
    formatos = ["Hola {}", "Bienvenido {}", "Es genial verte {}", "Gusto de verte {}", "Saludos {}", "Encantado de conocerte {}"]
    return random.choice(formatos)

def hola(nombre: str) -> str:
    if nombre == "":
        return "Error: nombre vacio."
    saludo = formato_aleatorio().format(nombre)
    return saludo

def holas(nombres: list[str]):
    saludos: dict[str, str] = {}
    for nombre in nombres:
        saludos[nombre] = hola(nombre)
    return saludos

print(hola("adrian"))
print(holas(["juan", 'paco', 'pedro', 'amelia', 'miyonette']))