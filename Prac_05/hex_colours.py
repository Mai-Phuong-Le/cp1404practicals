
"""
CP1404/CP5632 Practical
Hexadecimal colours
"""

COLOUR_TO_CODE = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "black": "#000000",
    "blue": "#0000ff",
    "coral": "#ff7f50",
    "darkgreen": "#006400",
    "gold": "#ffd700",
    "green": "#008000",
    "red": "#ff0000",
    "white": "#ffffff"
}

print(COLOUR_TO_CODE)
colour_name = input("Enter colour name: ").title()

while colour_name != "":
    try:
        print(colour_name, "is", COLOUR_TO_CODE[colour_name])
    except KeyError:
        print("Invalid colour name")
        colour_name = input("Enter colour name: ").title()

print(COLOUR_TO_CODE)