
"""
CP1404/CP5632 Practical
Hexadecimal colours
"""

COLOUR_TO_HEX = {
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

colour_name = input("Enter colour name: ").lower()

while colour_name != "":
    try:
        print(COLOUR_TO_HEX[colour_name])
    except KeyError:
        print("Invalid colour name")

    colour_name = input("Enter colour name: ").lower()