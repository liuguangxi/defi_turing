def solve():
    """
    Solves the twin numbers problem on a 28-row by 37-column table.
    - Table A is filled row-major: A(i, j) = i * 37 + (j + 1)
    - Table B is filled column-major: B(i, j) = j * 28 + (i + 1)
    Where 0 <= i < 28 and 0 <= j < 37.
    A twin is a cell (i, j) where A(i, j) == B(i, j).
    """
    ROWS = 28
    COLS = 37
    twins = []

    # Iterate through all cells in the 28x37 table
    for i in range(ROWS):
        for j in range(COLS):
            # Calculate value using row-major filling
            # (row index * total columns + current column number)
            val_row_major = i * COLS + (j + 1)

            # Calculate value using column-major filling
            # (column index * total rows + current row number)
            val_col_major = j * ROWS + (i + 1)

            if val_row_major == val_col_major:
                twins.append(val_row_major)

    return sum(twins)

print(solve())
