def rotate_list(some_list):
    """Take a list as input and remove the first item from the list and add it
        to the end of the list. Return the item moved"""
    x = some_list.pop(0)
    some_list.append(x)
    return x
    
fruits = ['apples', 'grapes', 'peaches', 'apricots', 'bananas']
print(f"Our list is:\n{fruits}")
print(f"Removed first item is: {rotate_list(fruits)}")
print(f"Our rotated list is:\n{fruits}")    