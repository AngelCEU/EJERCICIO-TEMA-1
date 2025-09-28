def calcular_estadisticas(notas):
    if not notas:
        print("La lista de notas está vacía.")
        return

    media = sum(notas) / len(notas)
    nota_max = max(notas)
    nota_min = min(notas)

    print(f"Media: {media:.2f}")
    print(f"Nota más alta: {nota_max}")
    print(f"Nota más baja: {nota_min}")

    if any(nota < 5 for nota in notas):
        print("Hay al menos una nota suspensa (<5).")

if __name__ == "__main__":
    # Ejemplo de uso: puedes cambiar las notas aquí
    notas = [7, 4.5, 9, 6, 3]
    calcular_estadisticas(notas)