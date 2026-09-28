"""
CP1404/CP5632 - Practical
Program for temperature conversion
"""

def main():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)

def convert_C_to_F_vise_versa():
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = celsius * 9.0 / 5 + 32
            return f"Result: {fahrenheit:.2f} F"
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit : "))
            celsius = 5 / 9 * (fahrenheit - 32)
            return f"Result: {celsius:.2f} C"
        else:
            return "Invalid option"

    print("Thank you.")
    return None


main()
convert_C_to_F_vise_versa()
