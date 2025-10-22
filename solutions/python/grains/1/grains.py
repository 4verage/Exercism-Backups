def square(number):
    if number not in range(1, 65):
        raise ValueError("square must be between 1 and 64")
    else:
        grains = [1]
        for i in range(1, 65):
            grains.append(grains[i - 1] + grains[i - 1])
        return grains[number - 1]

def total():
    run = 0
    for i in range(1, 65):
        run += square(i)
    return run
