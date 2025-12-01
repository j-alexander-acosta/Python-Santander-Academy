def es_primo(numero: int) -> bool:
    """Devuelve True si numero es primo."""
    if numero <= 1:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False

    limite = int(numero ** 0.5) + 1
    for divisor in range(3, limite, 2):
        if numero % divisor == 0:
            return False

    return True


def main() -> None:
    try:
        valor = int(input("Introduce un número entero: "))
    except ValueError:
        print("Debes introducir un número entero válido.")
        return

    if es_primo(valor):
        print(f"{valor} es un número primo.")
    else:
        print(f"{valor} no es un número primo.")


if __name__ == "__main__":
    main()


