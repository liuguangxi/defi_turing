import itertools

def solve():
    """
    Calculates the sum of all five-digit numbers formed using each
    odd digit {1, 3, 5, 7, 9} exactly once.
    """
    digits = [1, 3, 5, 7, 9]
    perms = list(itertools.permutations(digits))

    total_sum = 0
    for p in perms:
        # Convert tuple of digits to an integer
        num = 0
        for d in p:
            num = num * 10 + d
        total_sum += num

    return total_sum

print(solve())
