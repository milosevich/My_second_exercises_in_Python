"""Take 2 lists as input and return a new list consisting of the elements
   of the first list followed by the elements of the second list"""
   
# Simple solution
def combine_lists1(one, two):
    return one + two
    
# Longer solution
def combine_lists2(one, two):
    combine_list = []
    combine_list += one
    combine_list += two
    return combine_list

# Solution using methods
def combine_lists3(one, two):
    combine_list = []
    combine_list.extend(one)
    combine_list.extend(two)
    return combine_list
    
numbers = [1, 2, 3, 4]
fruits = ['apples', 'bananas', 'grapes', 'peaches', 'apricots']
new_list1 = combine_lists1(numbers, fruits)
print(f"Result with simple solution is:\n {new_list1}")
new_list2 = combine_lists2(numbers, fruits)
print(f"Result with longer solution is:\n {new_list2}")
new_list3 = combine_lists3(numbers, fruits)
print(f"Result with solution using methods is:\n {new_list3}")