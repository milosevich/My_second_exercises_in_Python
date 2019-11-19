def power_list(numbers):
    """Given a list of numbers, return a new list where each element is the
        corresponding element of the list to the power of the list index"""
    return [j ** i for i, j in enumerate(numbers)]
    
print(f"Power the list index of [2, 2, 2, 2, 2, 2] list is:\n{power_list([2, 2, 2, 2, 2, 2])}")
print(f"Power the list index of [9, 6, 5, 4] list is:\n{power_list([9, 6, 5, 4])}")