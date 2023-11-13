def format_fixed_width(matrix, padding=2, widths=None):
    '''accepts rows of columns (as a list of lists) and returns a fixed-width formatted string representing the given rows'''
    padding = " " * padding
    column_widths = widths if widths else [
        max(len(cell) for cell in column)
        for column in zip(*matrix)
    ]
    return "\n".join(
        padding.join([
            cell.ljust(length)
            for cell, length in zip(row, column_widths)
        ]).rstrip()
        for row in matrix
    )

print(format_fixed_width([['green', 'red'], ['blue', 'purple']]))
rows = [['Robyn', 'Henry', 'Lawrence'], ['John', 'Barbara', 'Gross'], ['Jennifer', '', 'Bixler']]
print(format_fixed_width(rows, padding=3, widths=[10, 10, 10]))
