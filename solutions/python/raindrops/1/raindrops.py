def convert(number):
    returnString = ""
    if number % 3 == 0:
        returnString += "Pling"
    if number % 5 == 0:
        returnString += "Plang"
    if number % 7 == 0:
        returnString += "Plong"

    if len(returnString) > 0:
        return returnString
    else:
        return str(number)
