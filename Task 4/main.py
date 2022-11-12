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
    "dedas55",
    "a",
    "ded",
    "cdcdf",
]


def add_frame(canvas):
    longest_word = canvas[0]
    for element in canvas:
        if len(element) > len(longest_word):
            longest_word = element
    for y_axis in range(0, len(canvas)):
        frame = ""
        for x_axis in range(0, len(longest_word)+2-len(canvas[y_axis])):
            # print(len(longest_word)-len(canvas[y_axis])+1)
            frame = frame + "*"
            if x_axis == (len(longest_word)+2-len(canvas[y_axis]))/2-1:
                # print("skirtumas", (len(longest_word)-len(canvas[y_axis]))/2)
                frame = frame + canvas[y_axis]
        if (len(longest_word)-len(canvas[y_axis])) == 0:
            frame = "*"+canvas[y_axis]+"*"
        print(frame)


add_frame(canvas)
