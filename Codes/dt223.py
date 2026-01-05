import math

def combinations(n, k):
    """Calculates the binomial coefficient nCr."""
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    if k > n // 2:
        k = n - k

    numerator = 1
    for i in range(k):
        numerator = numerator * (n - i) // (i + 1)
    return numerator

def solve():
    """
    Solves Moser's circle problem for n = 100 points.
    The maximum number of regions R(n) formed by connecting n points on a
    circle is given by the formula:
    R(n) = (n choose 4) + (n choose 2) + 1
    This corresponds to the sum of the first 5 terms of the (n-1)-th row
    of Pascal's triangle.
    """
    n = 100
    # R(100) = combinations(100, 4) + combinations(100, 2) + 1
    regions = combinations(n, 4) + combinations(n, 2) + 1
    return regions

print(solve())
