import random

def generar_adn(n):
    bases = ['A', 'T', 'C', 'G']
    cadena = ''.join(random.choices(bases, k=n))
    conteo = {base: cadena.count(base) for base in bases}
    return cadena, conteo

# Ejemplo de uso
if __name__ == "__main__":
    longitud = 20
    adn, conteo = generar_adn(longitud)
    print(f"Cadena de ADN: {adn}")
    print("Conteo de bases:", conteo)