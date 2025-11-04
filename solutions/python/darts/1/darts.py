import math

def score(x, y):
    # Define Circles
    circle1 = 1 ** 2
    circle2 = 5 ** 2
    circle3 = 10 ** 2

    # Define hit relative to center
    hit = (x ** 2) + (y ** 2)

    # Determie Points
    if hit <= circle1:
        return 10
    if hit <= circle2:
        return 5
    if hit <= circle3:
        return 1
    else:
        return 0

    
