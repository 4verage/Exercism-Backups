def rebase(input_base, digits, output_base):
    # Tests
    if input_base < 2:
        raise ValueError("input base must be >= 2")

    if output_base < 2:
        raise ValueError("output base must be >= 2")

    for num in digits:
        if num >= input_base or (num < input_base and 0 > num):
            raise ValueError("all digits must satisfy 0 <= d < input base")
    
    # Convert to Base10
    base_10 = 0
    for i, num in enumerate(digits):
        base_10 += (num * (input_base ** (len(digits) - (i + 1))))
    
    if output_base == 10:
        return [int(char) for char in str(base_10)]
    
    # Convert to Output Base
    quotient = base_10
    remainders = []
    while quotient >= 1:
        remainders.append(quotient % output_base)
        quotient = quotient // output_base

    # Ensure at least one value if None (zero)
    if len(remainders) == 0:
        remainders.append(0)

    return list(reversed(remainders))
    

    