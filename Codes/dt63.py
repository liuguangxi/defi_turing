import math

def solve():
    count = 0
    # For a^n to have n digits, 10^(n-1) <= a^n < 10^n
    # The second inequality a^n < 10^n implies a < 10.
    # Since n >= 1, and the number is a positive integer, a can be 1, 2, ..., 9.
    for a in range(1, 10):
        # We solve 10^(n-1) <= a^n for n:
        # (n-1) * log10(10) <= n * log10(a)
        # n - 1 <= n * log10(a)
        # 1 >= n * (1 - log10(a))
        # n <= 1 / (1 - log10(a))
        n_max = int(1 / (1 - math.log10(a)))
        count += n_max
    return count

print(solve())
