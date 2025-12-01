def calcular(operacion, num1, num2):
    """Ejecuta la operación matemática solicitada."""
    if operacion == "suma":
        return num1 + num2
    elif operacion == "resta":
        return num1 - num2
    elif operacion == "multiplicación" or operacion == "multiplicacion":
        return num1 * num2
    elif operacion == "división" or operacion == "division":
        if num2 == 0:
            return None  # Indica división por cero
        return num1 / num2
    else:
        return None  # Operación no válida


def main():
    """Función principal que ejecuta el bucle de la calculadora."""
    print("=== Calculadora ===")
    print("Operaciones disponibles: suma, resta, multiplicación, división")
    print("Escribe 'salir' para terminar el programa.\n")
    
    while True:
        # Pedir operación
        operacion = input("Ingresa la operación (o 'salir' para terminar): ").strip().lower()
        
        # Verificar si el usuario quiere salir
        if operacion == "salir":
            print("¡Hasta luego!")
            break
        
        # Validar que la operación sea válida
        operaciones_validas = ["suma", "resta", "multiplicación", "multiplicacion", 
                              "división", "division"]
        if operacion not in operaciones_validas:
            print("Operación no válida. Por favor, ingresa: suma, resta, multiplicación o división.\n")
            continue
        
        # Pedir los dos números
        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("Error: Por favor ingresa números válidos.\n")
            continue
        
        # Ejecutar la operación
        resultado = calcular(operacion, num1, num2)
        
        # Mostrar resultado o mensaje de error
        if resultado is None:
            if operacion in ["división", "division"]:
                print("Error: No se puede dividir por cero.\n")
            else:
                print("Error: Operación no válida.\n")
        else:
            print(f"Resultado: {resultado}\n")


if __name__ == "__main__":
    main()




