COLOR_NAMES = {"Absolute Zero": "#0048ba", "Baby Blue": "#89cff0", "Cadet Grey": "#91a3b0", "Dandelion": "#f0e130",
               "Deep Peach": "Deep Peach", "Earth Yellow": "#e1a95f", "Fawn": "#e5aa70", "Ginger": "#b06500",
               "Han Blue": "#446ccf", "Hollywood Cerise": "#f400a1"}

while True:
    try:
        color_name = input("Enter color name: ").title()
        code = COLOR_NAMES[color_name]
        print(f"{color_name}: {code}")
    except KeyError:
        print("Invalid color name")