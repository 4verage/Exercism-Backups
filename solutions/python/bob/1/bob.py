def response(hey_bob):
    hey_bob = hey_bob.strip()
    print(hey_bob)
    if hey_bob == "":
            return "Fine. Be that way!"
    if any(char.isalpha() for char in hey_bob):
        print("Has alpha characters...")
        if hey_bob.upper() == hey_bob and hey_bob[len(hey_bob) - 1] == '?':
            return "Calm down, I know what I'm doing!"
        if hey_bob.upper() == hey_bob:
            return "Whoa, chill out!"
    if hey_bob[len(hey_bob) - 1] == '?':
            return "Sure."
    return "Whatever."
