import string

def is_pangram(sentence):
    characters = list(string.ascii_lowercase)
    for letter in sentence.lower():
        if letter in characters:
            characters.remove(letter)
    if len(characters) > 0:
        return False
    else:
        return True
