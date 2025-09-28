def clasificar_personajes(personajes):
    """
    Recibe un diccionario {nombre: tipo} y devuelve:
    - Lista de humanos ordenados alfabéticamente.
    - Lista de criaturas ordenadas por longitud de nombre.
    """
    humanos = [nombre for nombre, tipo in personajes.items() if tipo == "humano"]
    criaturas = [nombre for nombre, tipo in personajes.items() if tipo == "criatura"]

    humanos_ordenados = sorted(humanos)
    criaturas_ordenadas = sorted(criaturas, key=len)

    return humanos_ordenados, criaturas_ordenadas

# Ejemplo de uso:
if __name__ == "__main__":
    personajes = {
        "Harry": "humano",
        "Hermione": "humano",
        "Dobby": "criatura",
        "Ron": "humano",
        "Centauro": "criatura",
        "Hagrid": "criatura"
    }

    humanos, criaturas = clasificar_personajes(personajes)
    print("Humanos ordenados:", humanos)
    print("Criaturas ordenadas:", criaturas)