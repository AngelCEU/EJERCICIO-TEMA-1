def clasificar_numeros(lista):
    pares = []
    impares = []
    negativos = []
    for numero in lista:
        if numero < 0:
            negativos.append(numero)
        elif numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares, negativos

# Ejemplo de uso
numeros = [1, -2, 3, 4, -5, 6, 0, -8]
pares, impares, negativos = clasificar_numeros(numeros)
print("Pares:", pares)
print("Impares:", impares)
print("Negativos:", negativos)