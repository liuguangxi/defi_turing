import math

def solve():
    # Precompute 17th powers for integers up to 10500 to cover all possible values of a, b, and c.
    # Since a, b <= 10000, c_max = (10000^17 + 10000^17)^(1/17) = 10000 * 2^(1/17) ≈ 10416.
    powers = [i**17 for i in range(10500)]

    best_diff = -1
    best_s = -1
    best_prod = 0

    # Iterate through all pairs (a, b) with 100 <= a < b <= 10000.
    # To optimize, we fix b and search for c that might correspond to a valid a.
    # Since a^17 + b^17 ≈ c^17 and a < b, c must be between b + 1 and floor(b * 2^(1/17)) + 1.
    ratio = 2**(1/17)

    for b in range(101, 10001):
        b17 = powers[b]

        # c must be slightly larger than b.
        # Max c happens when a is as large as possible (a = b-1).
        c_min = b + 1
        c_max = int(b * ratio) + 1

        for c in range(c_min, c_max + 1):
            c17 = powers[c]

            # For this b and c, find the ideal a such that a^17 ≈ c^17 - b^17.
            a_pow17 = c17 - b17

            # Since a must be at least 100, we skip if the difference is too small.
            if a_pow17 < powers[100]:
                continue

            # Find the integer closest to the 17th root of the difference.
            # Python's pow(int, float) handles large integers by converting to float,
            # which provides enough precision (~15-17 digits) to correctly round to
            # the nearest integer when the root is around 10^4.
            a_float = a_pow17**(1/17)
            a_low = int(a_float)
            a_high = a_low + 1

            # Check the two closest candidates for a.
            for a_cand in [a_low, a_high]:
                if 100 <= a_cand < b:
                    s = powers[a_cand] + b17
                    diff = abs(s - c17)

                    # Smallest relative error: |LHS - RHS| / LHS.
                    # Comparison diff / s < best_diff / best_s is equivalent to:
                    # diff * best_s < best_diff * s.
                    if best_prod == 0 or diff * best_s < best_diff * s:
                        best_diff = diff
                        best_s = s
                        best_prod = a_cand * b

    return best_prod

print(solve())
