def solve():
    """
    Given n, F(n) is the sum of natural integers x such that x^2 + n is a square.
    x^2 + n = y^2  =>  y^2 - x^2 = n  =>  (y - x)(y + x) = n.
    Let d1 = y - x and d2 = y + x.
    Then d1 * d2 = n, d2 >= d1, and d1, d2 must have the same parity.
    We are looking for the sum of F(n) for n = 1 to 1,000,000.

    Total sum S = sum_{n=1}^{N} F(n) = sum_{n=1}^{N} sum_{x^2 + n = y^2} x.
    This can be rewritten by changing the order of summation to iterate over
    divisors d1 and d2 such that d1*d2 <= N, d2 >= d1, and d1 == d2 (mod 2).
    x is given by (d2 - d1) / 2.

    Let d2 = d1 + 2k, where k >= 0 is an integer.
    Then x = k.
    The condition d1 * d2 <= N becomes d1 * (d1 + 2k) <= N, which simplifies to:
    2k * d1 <= N - d1^2  =>  k <= (N - d1^2) / (2 * d1).
    Since x = k = 0 does not contribute to the sum, we iterate k from 1 up to
    K = floor((N - d1^2) / (2 * d1)).
    For a fixed d1, the sum of x is 1 + 2 + ... + K = K * (K + 1) / 2.
    The maximum possible value for d1 occurs when d1^2 <= N, so d1 <= sqrt(N).
    """
    limit = 1000000
    total_sum = 0
    # Iterating d1 from 1 up to sqrt(limit)
    # limit = 10^6, so d1 max is 1000.
    for d1 in range(1, 1001):
        # Calculate the maximum number of steps k
        k = (limit - d1 * d1) // (2 * d1)
        if k > 0:
            # Sum of x values (1 + 2 + ... + k)
            total_sum += k * (k + 1) // 2

    return total_sum

print(solve())
