from fractions import Fraction

def solve():
    N = 1000000
    # Sum of 1/k for k from 2 to 11
    s = sum(Fraction(1, k) for k in range(2, 12))
    # n10 = N / (2 * s)
    n10 = Fraction(N) / (2 * s)
    return int(round(float(n10)))

print(solve())
