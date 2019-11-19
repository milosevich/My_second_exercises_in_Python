def dash_stringify(word_list):
    """Given a list of word strings, return a single string with all the
        strings together, with ' - ' in between the words."""
    return ' - '.join(word_list)

print(dash_stringify(['A', 'B', 'C']))