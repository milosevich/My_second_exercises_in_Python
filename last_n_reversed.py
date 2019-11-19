def last_n_reversed(sequence, n):
    """Given a sequence and a number n, return the last n elements of the
        sequence in reversed order"""
    return sequence[-1:-n-1:-1]
    
fruits = ['apples', 'grapes', 'peaches', 'apricots', 'bananas']
print(last_n_reversed(fruits, 3))
