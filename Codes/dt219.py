import math

def reverse_int(n):
    """Returns the integer formed by reversing the digits of n."""
    return int(str(n)[::-1])

def solve():
    """
    Finds two pairs of 4-digit numbers (a, b) and (c, d) such that their
    arithmetic mean A and geometric mean G are integers and are digit-reversals
    of each other.

    The property:
    A = (x + y) / 2
    G = sqrt(x * y)
    A = reverse(G)

    This implies x and y are roots of the quadratic equation t^2 - 2At + G^2 = 0.
    The discriminant D = (2A)^2 - 4G^2 = 4(A^2 - G^2) must be a perfect square,
    say (2k)^2. Thus A^2 - G^2 = k^2.
    The numbers are x = A - k and y = A + k.
    """
    results = []

    # Since a, b are 4-digit numbers (1000-9999), their geometric mean G
    # and arithmetic mean A must also be 4-digit integers.
    # Note: sqrt(1000*1001) > 1000 and (9999+9998)/2 < 9999.
    for g in range(1001, 10000):
        # A 4-digit integer reversed is still 4 digits unless it ends in 0.
        if g % 10 == 0:
            continue

        a_mean = reverse_int(g)

        # A must be greater than G for distinct numbers x and y.
        if a_mean <= g:
            continue

        # Check if A^2 - G^2 is a perfect square.
        k2 = a_mean**2 - g**2
        k = math.isqrt(k2)
        if k * k == k2:
            num1 = a_mean - k
            num2 = a_mean + k

            # Ensure the roots are 4-digit numbers.
            if 1000 <= num1 <= 9999 and 1000 <= num2 <= 9999:
                results.append((num1, num2))

    # Calculated values:
    # Pair 1: (3645, 7605) -> A=5625, G=5265
    # Pair 2: (3232, 9898) -> A=6565, G=5656
    # Answer: 3645 * 7605 + 3232 * 9898
    total_sum = 0
    for x, y in results:
        total_sum += x * y

    return total_sum

print(solve())
