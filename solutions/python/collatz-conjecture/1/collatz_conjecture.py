def steps(number):
    # Number must be greater than zero
    if number > 0:
    
        steps = 0
        while number != 1:
    
            # If number is positive
            if number % 2 == 0:
                number = number / 2
                steps += 1
    
            # If number is odd
            elif number % 2 != 0:
                number = number * 3 + 1
                steps += 1
    
        return steps

    else:

        raise ValueError("Only positive integers are allowed")
