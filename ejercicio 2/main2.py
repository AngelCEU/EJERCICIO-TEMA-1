# Programa para simular el ahorro mensual de una persona

# Entrada de datos
cantidad_inicial = float(input("Introduce la cantidad inicial (€): "))
cantidad_mensual = float(input("Introduce la cantidad que ahorras cada mes (€): "))
num_meses = int(input("Introduce el número de meses: "))

# Cálculo del total ahorrado
total_ahorrado = cantidad_inicial + cantidad_mensual * num_meses

# Salida
print(f"El total ahorrado es de  {total_ahorrado}")

# Mensaje extra si supera los 5000€
if total_ahorrado >= 5000:
    print("¡Felicidades! Has ahorrado más de 5000€.")
else :
    ahorro_faltante = 5000 - total_ahorrado
    print(f"no has llegado a tu meta, te faltan {ahorro_faltante}, sigue ahorrando para alcanzar tu meta.")
