def add(*matrix):
    '''accepts any number of lists-of-lists of numbers
       and returns one list-of-lists
       with each of the corresponding numbers in the given lists-of-lists added together'''
    rows = [
            row
            for row in zip(*matrix)
    ]
    return [
            [sum(value) for value in zip(*row)]
            for row in rows
    ]

matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
print(add(matrix1, matrix2))
