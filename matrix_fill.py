def matrix_fill(n_rows, n_cols):
    """Given number of rows and number of columns, create a matrix (list of
        lists) where each element is sequentially numbered"""
    return [
        [y + n_cols * x for y in range(1, n_cols+1)]
        for x in range(0, n_rows)
    ]
    
my_matrix = matrix_fill(5, 3)
print(my_matrix)
