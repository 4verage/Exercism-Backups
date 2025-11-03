def value(colors):
    return_value = ""
    vals = color()
    for col in range(2):
        return_value += str(vals.index(colors[col]))
    return int(return_value)

def color():
    return ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
