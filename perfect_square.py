def is_perfect_square(number):
    """Given a number, return True if it is a perfect square,
        else return False"""
    num = number ** 0.5
    return num.is_integer()

number = int(input("Input number to see is it a perfect square:"))
print(is_perfect_square(number))