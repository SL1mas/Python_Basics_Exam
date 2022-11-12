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
    pass


longest_word = canvas[0]
print("pirmas", longest_word)
for element in canvas:
    print(element)
    if len(element) > len(longest_word):
        longest_word = element
print("Ilgiausias", longest_word)
# print("Vyriausio vartotojo amžius:", longest_word)
