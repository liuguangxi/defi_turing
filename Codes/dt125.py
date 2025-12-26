import collections

def solve():
    # The number of cubes in the k-th layer of an a x b x c parallelepiped is
    # n = 2(ab + bc + ca) + 4(a + b + c)(k - 1) + 4(k - 1)(k - 2)
    # Let m = n / 2, and d = k - 1. Then:
    # m = ab + bc + ca + 2d(a + b + c) + 2d(d - 1)
    # with a >= b >= c >= 1 and d >= 0.

    limit = 2000  # Initial guess for the range of m
    counts = collections.defaultdict(int)

    # d is small since m is roughly 2*d^2
    for d in range(40):
        # Contribution from terms containing d
        base_d = 2 * d * (d - 1)
        if base_d > limit:
            break

        # Parallelepiped dimensions a, b, c
        # Since c <= b <= a and c*b + b*a + a*c grows quickly:
        for c in range(1, 50):
            for b in range(c, 1000):
                # Smallest m for this d, c, b occurs at a = b
                m_min = b*c + b*b + b*c + 2*d*(b + b + c) + base_d
                if m_min > limit:
                    break

                # m = a(b + c + 2d) + (bc + 2d(b + c) + 2d(d - 1))
                # m = a*X + Y
                X = b + c + 2 * d
                Y = b * c + 2 * d * (b + c) + base_d

                # We need a >= b and m <= limit
                # a*X + Y <= limit  => a <= (limit - Y) / X
                a_start = b
                a_end = (limit - Y) // X

                if a_end >= a_start:
                    # For all 'a' in [a_start, a_end], compute m and increment count
                    # Optimized loop to just add counts for the calculated values
                    for a in range(a_start, a_end + 1):
                        m = a * X + Y
                        counts[m] += 1

    # Find the smallest n = 2*m such that counts[m] == 100
    candidates = [2 * m for m, count in counts.items() if count == 100]
    return min(candidates) if candidates else None

print(solve())
