def translate(text):

    words = text.split(' ')
    returned = ""

    for word in words:

        vowels = ['a', 'e', 'i', 'o', 'u', 'y']
        safe_starts = ['xr', 'yt']
    
        # Rule 1
        if word[0] in vowels or word[0:2] in safe_starts:
            # Rule 4
            if word[0] == 'y' and word[0:2] not in safe_starts:
                returned = returned + word[1:] + 'yay' + ' '
                continue
            returned = returned + word + 'ay' + ' '
            continue
    
        # Rule 2
        letters = ""
        position = 0
        for index, letter in enumerate(word):
            if letter not in vowels and word[index:index + 2] != 'qu':
                letters = letters + letter
                position += 1
            else:
                break
        if word[position:position + 2] != 'qu':
            returned = returned + word[position:] + letters + 'ay' + ' '
            continue
    
        # Rule 3
        if word[position:position + 2] == 'qu':
            letters = letters + 'qu'
            position = position + 2
            returned = returned + word[position:] + letters + 'ay' + ' '
            continue

    returned = returned.strip()
    return returned
