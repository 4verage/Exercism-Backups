def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    # Throw an error if the number given is not positive.
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    # Get factors
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    factors = list(set(factors))
    factors.remove(number)

    # Calculate
    factor_sum = sum(fact for fact in factors)
    
    # Return type
    if factor_sum == number:
        return "perfect"
    if factor_sum > number:
        return "abundant"
    if factor_sum < number:
        return "deficient"
