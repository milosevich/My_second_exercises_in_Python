def last_n_elements(sequence, n):
    """Given a sequence and a number n, return the last n elements of the
        sequence"""
    return sequence[-n:]

fruits = ['apples', 'grapes', 'peaches', 'apricots', 'bananas']
print(last_n_elements(fruits, 3))