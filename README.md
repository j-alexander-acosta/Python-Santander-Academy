## Descripción del proyecto

Este repositorio contiene varios ejercicios y scripts escritos en Python, pensados para practicar programación básica y manejo de entrada/salida:

- **`FizzBuzz.py` / `FizzBuzz`**: Imprime los números del 1 al 50, sustituyendo múltiplos de 3 por "Fizz", de 5 por "Buzz" y de ambos por "FizzBuzz".
- **`Calculadora.py`**: Calculadora en consola que permite realizar operaciones de suma, resta, multiplicación y división entre dos números.
- **`primos.py`**: Comprueba si un número entero introducido por el usuario es primo o no.
- **`prueba.py`**: Captura datos básicos de un usuario (signos vitales y otros) y calcula métricas como IMC y valores normalizados.
- **`contador_palabras/contador.py`**: Cuenta el número total de palabras de un archivo de texto y muestra las 10 más frecuentes.

Cada script es independiente y se puede ejecutar por separado.

## Requisitos

- **Python** 3.11 o superior (cualquier versión 3.x reciente debería funcionar).
- Sistema operativo probado: **macOS** (aunque debería funcionar también en Windows y Linux con Python instalado).

Opcionalmente, puedes usar un entorno virtual (por ejemplo, el que ya existe en `contador_palabras/venv`) para aislar las dependencias, aunque estos scripts usan solo la librería estándar de Python.

## Instalación

1. **Clonar el repositorio** (o descargar el proyecto):

```bash
git clone <URL_DE_TU_REPOSITORIO>
cd Cursor
```

2. *(Opcional)* **Crear y activar un entorno virtual**:

```bash
python3 -m venv venv
source venv/bin/activate  # En macOS / Linux
# En Windows (PowerShell):
# venv\Scripts\Activate.ps1
```

No es necesario instalar paquetes adicionales, ya que todo el código usa solo la biblioteca estándar de Python.

## Instrucciones de uso

### FizzBuzz (`FizzBuzz.py`)

Ejecuta el script para mostrar la secuencia FizzBuzz del 1 al 50:

```bash
python3 FizzBuzz.py
```

En algunos entornos también puedes tener un archivo ejecutable llamado `FizzBuzz` con el mismo contenido.

### Calculadora (`Calculadora.py`)

Calculadora interactiva por consola:

```bash
python3 Calculadora.py
```

Uso:
- El programa mostrará las operaciones disponibles: **suma**, **resta**, **multiplicación**, **división**.
- Escribe el nombre de la operación cuando se te solicite.
- Introduce los dos números cuando el programa lo pida.
- Escribe `salir` para terminar el programa.

### Comprobación de números primos (`primos.py`)

Comprueba si un número entero es primo:

```bash
python3 primos.py
```

El programa:
- Pedirá un número entero.
- Mostrará si el número es o no es primo.

### Captura de datos de usuario (`prueba.py`)

Captura datos básicos de una persona y calcula algunos indicadores:

```bash
python3 prueba.py
```

El programa:
- Solicita nombre, edad, sexo, altura, peso, presión arterial, frecuencia cardiaca, frecuencia respiratoria, temperatura, saturación de oxígeno, diagnóstico y tratamiento.
- Calcula el **IMC** (Índice de Masa Corporal) y otras métricas normalizadas.
- Imprime los resultados y los datos introducidos.

### Contador de palabras (`contador_palabras/contador.py`)

Cuenta las palabras en un archivo de texto y muestra las más frecuentes:

```bash
cd contador_palabras
python3 contador.py
```

El programa:
- Te pedirá la ruta de un archivo de texto (por ejemplo, `/ruta/al/archivo.txt`).
- Leerá el contenido del archivo.
- Contará el número total de palabras.
- Mostrará el total y las **10 palabras más frecuentes** con su contador.

## Notas adicionales

- Todos los scripts están pensados para ejecutarse desde la línea de comandos.
- Si tienes varias versiones de Python instaladas, puede que necesites usar `python` en lugar de `python3` en los comandos.
- Puedes modificar y ampliar los scripts libremente para seguir practicando Python.


