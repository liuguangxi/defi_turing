import math

def solve():
    """
    Finds the sum of G(n) = gcd(A(n), B(n)) for n from 3 to 10,000.
    Based on the formulas provided in the hint:
    A(n) = 3 * 4^(n-1) - 2 * 3^(n-1)
    B(n) = 4^(n-2) * (18*n - 138) + 3^(n-1) * (4*n + 26)

    Algebraic reduction of the GCD:
    2*B(n) = 4^(n-1) * (9*n - 69) + 3^(n-1) * (8*n + 52)
    Using the identity 3 * 4^(n-1) = A(n) + 2 * 3^(n-1):
    6*B(n) = (3 * 4^(n-1)) * (9*n - 69) + 3 * 3^(n-1) * (8*n + 52)
           = (A(n) + 2 * 3^(n-1)) * (9*n - 69) + 3^n * (8*n + 52)
           = A(n) * (9*n - 69) + 3^(n-1) * (18*n - 138 + 24*n + 156)
           = A(n) * (9*n - 69) + 3^(n-1) * (42*n + 18)
           = A(n) * (9*n - 69) + 3^(n-1) * 6 * (7*n + 3)

    Since G(n) = gcd(A(n), B(n)) and A(n) is always even (for n >= 2),
    G(n) is even and satisfies G(n) = gcd(A(n), 2*B(n)).
    Furthermore, G(n) = gcd(A(n), 6 * (7*n + 3) * 3^(n-1)).
    Since gcd(A(n), 3^(n-1)) = 3 (for n >= 2), the power of 3 dividing the GCD is at most 3^1.
    Thus, G(n) simplifies to gcd(A(n), 6 * (7*n + 3)).
    """
    total_sum = 0
    # Iterate through the range specified in the problem
    for n in range(3, 10001):
        # The limit derived from the linear reduction above
        m = 42 * n + 18

        # Calculate A(n) modulo m to compute the GCD efficiently
        # A(n) = 3 * 4^(n-1) - 2 * 3^(n-1)
        term1 = (3 * pow(4, n - 1, m)) % m
        term2 = (2 * pow(3, n - 1, m)) % m
        an_mod_m = (term1 - term2) % m

        # Add the GCD for the current order n to the total
        total_sum += math.gcd(an_mod_m, m)

    return total_sum

print(solve())
