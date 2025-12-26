import itertools

def solve():
    # The first eight odd numbers
    odds = [1, 3, 5, 7, 9, 11, 13, 15]
    # The positions are 1st, 2nd, ..., 8th row, used as coefficients 2, 4, ..., 16
    coefficients = [2, 4, 6, 8, 10, 12, 14, 16]

    max_product = -float('inf')

    # Iterate through all permutations of the eight odd numbers
    # 8! = 40,320 is small enough for brute force
    for x in itertools.permutations(odds):
        current_product = 1
        for i in range(8):
            current_product *= (coefficients[i] - x[i])

        if current_product > max_product:
            max_product = current_product

    return max_product

print(solve())
