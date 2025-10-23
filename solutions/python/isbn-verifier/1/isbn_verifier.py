def is_valid(isbn):
    # Get rid of the dashes (if any)
    isbn = isbn.replace('-', '')

    # Confirm Length
    if len(isbn) != 10:
        return False

    # Array
    d = list(isbn)

    # Purely for math readability
    d.insert(0, '0')

    # Convert any ending 'X' to 10
    if d[len(d) - 1] == 'X':
        d[len(d) - 1] = '10'

    # Confirm numerals:
    for index in range(len(d)):
        if not d[index].isnumeric():
            return False

    # Convert to ints
    d = [int(i) for i in d]

    # Do math stuff
    return ((d[1] * 10 + d[2] * 9 + d[3] * 8 + d[4] * 7 + d[5] * 6 + d[6] * 5 + d[7] * 4 + d[8] * 3 + d[9] * 2 + d[10] * 1) % 11 == 0)
