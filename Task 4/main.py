# Turimas sąrašas, pvz.:

# canvas = [
#   "abc",
#   "ded"
# ]

# Sukurkite funkciją "addFrame", kuri pridėtų rėmelį ir grąžintų pamodifikuotą sąrašą:

# canvas_with_frame = [
#   "*****"
#   "*abc*",
#   "*ded*",
#   "*****"
# ]

# Pastaba: sąrašas gali ir neturėti nei vieno elemento arba turėtų tusčių elementų. pvz.
# canvas = [] arba canvas = [""]

# Jeigu sąrašas yra tusčias arba visi elementą tušti išmeskite klaidą - "Error: empty canvas provided".
# Beje, sąraše esantis tekstas, gali būti ir skirtingo ilgio. Todėl rėmelis turėtų būti brėžiamas pagal ilgiausią saraše esantį elementą.

canvas = [
    "abc",
    "dedas",
    "a",
    "dedasaxadfdf",
    "cdcdfvgrbcdcdcdc10",
]


def add_frame(canvas):
    longest_word = canvas[0]
    for element in canvas:
        if len(element) > len(longest_word):
            longest_word = element
    print("Ilgiausias", longest_word)
    print("X_axis", len(longest_word))
    print("Y_axis", len(canvas))
    for y_axis in range(0, len(canvas)):
        a = "*"
        # print("skirtumas", (len(longest_word)-len(canvas[y_axis]))/2)
        # print("*" + "*".join(canvas[y_axis]))
        # [print("x") for x_axis in range(0, len(longest_word))]
        for x_axis in range(0, len(longest_word)):
            a = a + "*"
        print(a)
        # print("ilgis", len(a))


add_frame(canvas)
