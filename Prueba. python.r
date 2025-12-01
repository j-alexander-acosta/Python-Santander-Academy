# Realizar la captura de los datos de un usuario
def capturar_datos_usuario():
    nombre = input("Ingrese su nombre: ")
    edad = input("Ingrese su edad: ")
    sexo = input("Ingrese su sexo: ")
    altura = input("Ingrese su altura: ")
    peso = input("Ingrese su peso: ")
    presion_arterial = input("Ingrese su presion arterial: ")
    frecuencia_cardiaca = input("Ingrese su frecuencia cardiaca: ")
    frecuencia_respiratoria = input("Ingrese su frecuencia respiratoria: ")
    temperatura = input("Ingrese su temperatura: ")
    saturacion_oxigeno = input("Ingrese su saturacion de oxigeno: ")
    diagnostico = input("Ingrese su diagnostico: ")
    tratamiento = input("Ingrese su tratamiento: ") 
    return nombre, edad, sexo, altura, peso, presion_arterial, frecuencia_cardiaca, frecuencia_respiratoria, temperatura, saturacion_oxigeno, diagnostico, tratamiento

# Realizar la captura de los datos de un usuario
nombre, edad, sexo, altura, peso, presion_arterial, frecuencia_cardiaca, frecuencia_respiratoria, temperatura, saturacion_oxigeno, diagnostico, tratamiento = capturar_datos_usuario()

# Realizar el calculo del IMC
imc = peso / (altura ** 2)

# Realizar el calculo de la presion arterial
presion_arterial = presion_arterial / 120

# Realizar el calculo de la frecuencia cardiaca