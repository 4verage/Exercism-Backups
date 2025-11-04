def is_armstrong_number(number):
    armstrong = 0
    for num in str(number):
        armstrong += int(num) ** len(str(number))
    return (armstrong == number)
