import math

def solve():
    """
    Finds the smallest n = x + y + z such that x > y > z > 0 and
    x+y, x-y, x+z, x-z, y+z, and y-z are all squares.

    Let x-y = b^2, y+z = e^2, and y-z = f^2.
    Then x+y = b^2 + e^2 + f^2 = a^2.
    Also x+z = b^2 + e^2 = c^2 and x-z = b^2 + f^2 = d^2.
    These equations imply:
    1) b^2 + e^2 = c^2
    2) b^2 + f^2 = d^2
    3) b^2 + e^2 + f^2 = a^2

    For x, y, z to be integers, e and f must have the same parity.
    If e, f were both odd, b^2 + e^2 + f^2 = a^2 would be b^2 + 2 = a^2 (mod 4),
    which is impossible for any integer b. Thus, e and f must both be even.
    This implies b must be odd for a primitive solution (one where gcd(x,y,z)=1).
    Since any non-primitive solution is a multiple of a primitive one by a square
    factor (n' = k^2 * n), the smallest n must come from the smallest primitive case.
    """
    min_n = float('inf')
    # Since n > b^2, to find n < 1006193, we only need to search b up to sqrt(1006193) ~ 1003.
    for b in range(1, 1005, 2):
        b2 = b * b
        evens = []

        # We need b^2 + e^2 = c^2.
        # Rearranging: (c-e)(c+e) = b^2.
        # Let k1 = c-e be a divisor of b^2 such that k1 < b.
        # Then c+e = b^2 / k1, so e = (b^2/k1 - k1) / 2.
        # Since b is odd, b^2 and k1 are odd, so e is always even.
        for k1 in range(1, b, 2):
            if b2 % k1 == 0:
                k2 = b2 // k1
                e = (k2 - k1) // 2
                evens.append(e)

        # We need at least two such even legs (e and f) to satisfy conditions 2 and 3.
        if len(evens) < 2:
            continue

        evens.sort()
        for i in range(len(evens)):
            e = evens[i]
            for j in range(i):
                f = evens[j]
                # Condition 3: b^2 + e^2 + f^2 must be a perfect square.
                a2 = b2 + e*e + f*f
                a = math.isqrt(a2)
                if a * a == a2:
                    # n = x + y + z = (2*b^2 + 3*e^2 + f^2) / 2
                    n = (2 * b2 + 3 * e*e + f*f) // 2
                    if n < min_n:
                        min_n = n

    return min_n

print(solve())
