def decodificar_mensaje(mensaje_cifrado):
    # Invertir el mensaje
    mensaje_invertido = mensaje_cifrado[::-1]
    # Eliminar caracteres especiales (solo letras y números)
    mensaje_decodificado = ''.join(c for c in mensaje_invertido if c.isalnum())
    return mensaje_decodificado

if __name__ == "__main__":
    mensaje = input("Introduce el mensaje cifrado: ")
    resultado = decodificar_mensaje(mensaje)
    print("Mensaje decodificado:", resultado)
    