"""CP1404 practical 5 hex colours exercise."""

NAME_TO_HEX = {"Aureolin": "#fdee00", "Army Green": "#4b5320", "Amber": "#ffbf00", "Amethyst": "#9966cc",
               "Acid Green": "#b0bf1a", "Aqua": "#00ffff", "Bole": "#79443b", "Blue Bell": "#a2a2d0",
               "Black Coffee": "#3b2f2f", "Champagne": "#f7e7ce"}

for name in NAME_TO_HEX:
    print(name)

colour_name = input("Enter colour name: ").title()
while colour_name != "":
    try:
        print(f"{colour_name} hex code: {NAME_TO_HEX[colour_name]}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").title()
