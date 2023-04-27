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
    "dedas555",
    "a",
    "dedg",
    "cdcdf",
]
canvas_with_frame = []


def add_frame(canvas):
    longest_word = canvas[0]
    for element in canvas:
        if len(element) > len(longest_word):
            longest_word = element
    for y_axis in range(0, len(canvas)):
        frame = ""
        x_axis_range_end = len(longest_word)+2-len(canvas[y_axis])
        if y_axis == 0 or y_axis == len(canvas)-1:
            for x_axis in range(0, len(longest_word)+2):
                frame = frame + "*"
            canvas_with_frame.append(frame)
            print(frame)
        frame = ""
        for x_axis in range(0, x_axis_range_end-1):
            frame = frame + "*"
            if x_axis == int(x_axis_range_end/2-1):
                if x_axis_range_end % 2 == 0:
                    frame = frame + canvas[y_axis] + "*"
                else:
                    frame = frame + canvas[y_axis] + " "
        if (x_axis_range_end-2) == 0:
            frame = "*"+canvas[y_axis]+"*"
        canvas_with_frame.append(frame)
        print(frame)
        frame = ""
        if y_axis == len(canvas)-1:
            for x_axis in range(0, len(longest_word)+2):
                frame = frame + "*"
            canvas_with_frame.append(frame)
            print(frame)
    return canvas_with_frame


if len(canvas) == 0 or [s.isspace() for s in canvas][len(canvas)-1] or canvas == [""]:
    print("Error: empty canvas provided")
else:
    add_frame(canvas)
    print(canvas_with_frame)
