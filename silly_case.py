def silly_case(in_string):
    """Given a string, convert it to a string such that each word starts with
        a lower case letter, and the remaining letters are uppercase.
        Return the silly case string."""
    silly_string = in_string.title().swapcase()
    return silly_string
    
silly = silly_case("This is a string FOR SILLY case.")
print(silly)
