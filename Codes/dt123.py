import itertools

def count_antimagic_completions():
    # Available numbers to fill the 10 empty squares (1 to 16 excluding existing ones)
    existing = {2, 4, 13, 14, 15, 16}
    available = [n for n in range(1, 17) if n not in existing]

    # Pre-calculated constant row/column values from the grid:
    # Row 4: 16, 15, 4, 2 -> Sum = 37
    # Row 3: x8, x9, 14, 13 -> Constant part = 27
    # Col 1: x0, x4, x8, 16 -> Constant part = 16
    # Col 2: x1, x5, x9, 15 -> Constant part = 15
    # Col 3: x2, x6, 14, 4 -> Constant part = 18
    # Col 4: x3, x7, 13, 2 -> Constant part = 15
    # Diag 1 (TL-BR): x0, x5, 14, 2 -> Constant part = 16
    # Diag 2 (TR-BL): x3, x6, x9, 16 -> Constant part = 16

    count = 0
    # Iterate through all permutations of available numbers (10! = 3,628,800)
    for p in itertools.permutations(available):
        x0, x1, x2, x3, x4, x5, x6, x7, x8, x9 = p

        # Calculate the 10 sums: 4 rows, 4 columns, 2 main diagonals
        sums = [
            x0 + x1 + x2 + x3,           # Row 1
            x4 + x5 + x6 + x7,           # Row 2
            x8 + x9 + 27,                # Row 3
            37,                          # Row 4
            x0 + x4 + x8 + 16,           # Col 1
            x1 + x5 + x9 + 15,           # Col 2
            x2 + x6 + 18,                # Col 3
            x3 + x7 + 15,                # Col 4
            x0 + x5 + 16,                # Diag 1
            x3 + x6 + x9 + 16            # Diag 2
        ]

        # Check if the 10 sums are distinct and consecutive
        if len(set(sums)) == 10 and max(sums) - min(sums) == 9:
            count += 1

    return count

print(count_antimagic_completions())
