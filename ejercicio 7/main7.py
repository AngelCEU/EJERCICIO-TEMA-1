from urllib.parse import urlparse

def analizar_url(url):
    try:
        parsed = urlparse(url)
        protocolo = parsed.scheme if parsed.scheme else None
        dominio = parsed.netloc if parsed.netloc else None
        # El nombre del recurso es la última parte del path, si existe
        recurso = parsed.path.split('/')[-1] if parsed.path and parsed.path != '/' else None
        return protocolo, dominio, recurso
    except Exception as e:
        print(f"Error al analizar la URL: {e}")
        return None, None, None

# Ejemplo de uso:
if __name__ == "__main__":
    url = "https://www.ejemplo.com/carpeta/archivo.html"
    protocolo, dominio, recurso = analizar_url(url)
    print("Protocolo:", protocolo)
    print("Dominio:", dominio)
    print("Recurso:", recurso)