# Realizar la captura de los datos de un usuario
def capturar_datos_usuario():
    nombre = input("Ingrese su nombre: ")
    edad = input("Ingrese su edad: ")
    sexo = input("Ingrese su sexo: ")
    altura = float(input("Ingrese su altura: "))
    peso = float(input("Ingrese su peso: "))
    presion_arterial = float(input("Ingrese su presion arterial: "))
    frecuencia_cardiaca = float(input("Ingrese su frecuencia cardiaca: "))
    frecuencia_respiratoria = float(input("Ingrese su frecuencia respiratoria: "))
    temperatura = float(input("Ingrese su temperatura: "))
    saturacion_oxigeno = float(input("Ingrese su saturacion de oxigeno: "))
    diagnostico = (input("Ingrese su diagnostico: "))
    tratamiento = (input("Ingrese su tratamiento: ")) 
    return nombre, edad, sexo, altura, peso, presion_arterial, frecuencia_cardiaca, frecuencia_respiratoria, temperatura, saturacion_oxigeno, diagnostico, tratamiento

# Realizar la captura de los datos de un usuario
nombre, edad, sexo, altura, peso, presion_arterial, frecuencia_cardiaca, frecuencia_respiratoria, temperatura, saturacion_oxigeno, diagnostico, tratamiento = capturar_datos_usuario()

# Realizar el calculo del IMC
imc = peso / (altura ** 2)

# Realizar el calculo de la presion arterial
presion_arterial = presion_arterial / 120

# Realizar el calculo de la frecuencia cardiaca
frecuencia_cardiaca = frecuencia_cardiaca / 120

# Realizar el calculo de la frecuencia respiratoria
frecuencia_respiratoria = frecuencia_respiratoria / 120

# Realizar el calculo de la temperatura
temperatura = temperatura / 120

# Realizar el calculo de la saturacion de oxigeno
saturacion_oxigeno = saturacion_oxigeno / 120


# Imprimir los resultados
print("El IMC del usuario es: ", imc)
print("La presion arterial del usuario es: ", presion_arterial)
print("La frecuencia cardiaca del usuario es: ", frecuencia_cardiaca)
print("La frecuencia respiratoria del usuario es: ", frecuencia_respiratoria)
print("La temperatura del usuario es: ", temperatura)
print("La saturacion de oxigeno del usuario es: ", saturacion_oxigeno)
print("El diagnostico del usuario es: ", diagnostico)
print("El tratamiento del usuario es: ", tratamiento)
