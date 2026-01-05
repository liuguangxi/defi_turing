import math

def gcd(a, b):
    """Compute the greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return a

def F(a, b, c):
    """
    Calculate the number of tiles crossed by a chord from (0,0) to (a,b)
    in a grid where grid lines are at x = k*c and y = m*c.

    The chord enters a new tile whenever it crosses a grid line.
    The number of vertical grid lines between 0 and a is floor((a-1)/c).
    The number of horizontal grid lines between 0 and b is floor((b-1)/c).
    The chord crosses both a vertical and a horizontal line at the same time
    if and only if there exist integers k, m such that k*c = (a/b) * m*c,
    which is equivalent to k*b = m*a.
    The number of such points (excluding the origin) is floor((gcd(a, b)-1)/c).

    The total number of tiles crossed is 1 + (total crossings) - (simultaneous crossings).
    """
    g = gcd(a, b)
    num_x_crossings = (a - 1) // c
    num_y_crossings = (b - 1) // c
    num_simultaneous = (g - 1) // c
    return 1 + num_x_crossings + num_y_crossings - num_simultaneous

def solve():
    """
    Calculate the sum of F(a, b, c) for the given ranges:
    4400 <= a <= 4600
    2300 <= b <= 2500
    10 <= c <= 60
    """
    total_sum = 0
    # Loop through the ranges inclusive of endpoints.
    # Note: 4400 > 2500 > 60, so a > b > c is always satisfied.
    for a in range(4400, 4601):
        for b in range(2300, 2501):
            g = gcd(a, b)
            # Sum F(a, b, c) across the range of c for each (a, b).
            for c in range(10, 61):
                total_sum += 1 + (a - 1) // c + (b - 1) // c - (g - 1) // c

    return total_sum

print(solve())
