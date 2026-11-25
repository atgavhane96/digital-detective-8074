"""Simple decimal-to-binary and decimal-to-hexadecimal number converter."""


def main() -> None:
    """Ask the user for a decimal number and display binary and hexadecimal conversions."""
    raw_input = input("Enter a decimal integer: ").strip()
    try:
        decimal_number = int(raw_input)
    except ValueError:
        print("Error: Please enter a valid whole decimal number.")
        return

    binary_output = bin(decimal_number)
    hexadecimal_output = hex(decimal_number)

    print(f"Decimal: {decimal_number}")
    print(f"Binary: {binary_output}")
    print(f"Hexadecimal: {hexadecimal_output}")


if __name__ == "__main__":
    main()
