import math

def gcd(a, b):
    """Computes the greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Computes the least common multiple of a and b."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)

def solve():
    """
    Calculates the sum of P(i, 10^i) for i from 1 to 1000.
    F(n) = k is the smallest k such that n + k is not divisible by k + 1.
    This condition is equivalent to:
    n - 1 is divisible by 2, 3, ..., k (i.e., n - 1 is a multiple of L_k)
    AND n - 1 is NOT divisible by k + 1 (i.e., n - 1 is not a multiple of L_{k+1}).

    P(s, N) is the number of integers n in (1, N) for which F(n) = s.
    The count is floor((N-2) / L_s) - floor((N-2) / L_{s+1}), where L_k = lcm(1, ..., k).
    """
    # Precompute L_k values up to 1001
    lums = [1] * 1002
    for k in range(2, 1002):
        lums[k] = lcm(lums[k-1], k)

    total_sum = 0
    # Sum P(i, 10^i) for i in [1, 1000]
    for i in range(1, 1001):
        n_minus_2 = 10**i - 2
        # Number of integers in {2, ..., 10^i - 1} satisfying the condition
        p_i = (n_minus_2 // lums[i]) - (n_minus_2 // lums[i+1])
        total_sum += p_i

    # Return the last 12 digits of the result
    return total_sum % 10**12

print(solve())
