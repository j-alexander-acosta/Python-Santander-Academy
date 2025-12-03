# Programa para contar palabras en un archivo de texto

# 1. Pedir al usuario la ruta de un archivo de texto.
archivo = input("Ingrese la ruta del archivo de texto: ")
try:
    with open(archivo, 'r', encoding='utf-8') as file:
        contenido = file.read()
except FileNotFoundError:
    print("El archivo no existe.")
    exit(1)
# 2. Leer el contenido del archivo.
# 3. Separar en palabras.
import re
palabras = re.findall(r'\b\w+\b', contenido)
# 4. Contar número total de palabras.
total_palabras = len(palabras)
print(f"El total de palabras es: {total_palabras}")
# 5. (Opcional) Mostrar las 10 palabras más frecuentes y su conteo.
from collections import Counter
contador_palabras = Counter(palabras)
print(contador_palabras.most_common(10))
