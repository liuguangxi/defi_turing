import itertools

def solve_heterogeneous_squares():
    # Numbers 1 to 9 to be placed in a 3x3 grid
    nums = range(1, 10)
    count = 0

    # Iterate through all 9! = 362,880 permutations
    for p in itertools.permutations(nums):
        # Calculate the 8 sums: 3 rows, 3 columns, and 2 diagonals
        sums = [
            p[0] + p[1] + p[2], # Row 1
            p[3] + p[4] + p[5], # Row 2
            p[6] + p[7] + p[8], # Row 3
            p[0] + p[3] + p[6], # Column 1
            p[1] + p[4] + p[7], # Column 2
            p[2] + p[5] + p[8], # Column 3
            p[0] + p[4] + p[8], # Diagonal 1
            p[2] + p[4] + p[6]  # Diagonal 2
        ]

        # A square is heterogeneous if all 8 sums are distinct
        if len(set(sums)) == 8:
            count += 1

    return count

print(solve_heterogeneous_squares())
