import math

def solve():
    """
    Geometry Analysis:
    - Let the rectangle have vertices at (0,b), (a,b), (a,0), and (0,0).
    - Fold lines start at the top corners (0,b) and (a,b).
    - The lower corners (0,0) and (a,0) are folded to coincide at a point P(a/2, y_P).
    - The fold line is the perpendicular bisector of the segment from (0,0) to P.
    - Let the fold line intersect the bottom edge at (x,0).
    - Using the distance property dist((0,b), (0,0)) = dist((0,b), P) and
      dist((x,0), (0,0)) = dist((x,0), P), we derive the relation:
      x = (a/2 * b) / (b + sqrt(b^2 - (a/2)^2))
    - For x to be an integer, 4b^2 - a^2 must be a perfect square k^2, and a must be even (a = 2A).
    - This leads to a Pythagorean triple (A, K, b) where A^2 + K^2 = b^2 and K = k/2.
    - The condition for x to be an integer becomes (b + K) | (A * b).

    Problem constraints:
    - a, b are non-zero natural numbers.
    - b <= 1,000,000.
    - a < 2b (always true for the leg A of a Pythagorean triple).
    """
    limit = 1000000
    # Use a set to count unique (a, b) pairs
    pairs = set()

    # Generate Pythagorean triples (A, K, b) using Euclid's formula for primitive triples
    # b = k(m^2 + n^2)
    m_limit = int(math.sqrt(limit)) + 1
    for m in range(2, m_limit):
        for n in range(1, m):
            if (m - n) % 2 == 1 and math.gcd(m, n) == 1:
                w = m*m + n*n
                if w > limit:
                    break

                u = m*m - n*n
                v = 2*m*n

                # Check both leg assignments: A=u, K=v and A=v, K=u
                # We need x = (k * leg * hyp) / (hyp + k_leg) to be an integer

                # Case 1: A = u, K = v
                denom1 = w + v
                num1 = u * w
                step1 = denom1 // math.gcd(num1, denom1)
                for k in range(step1, limit // w + 1, step1):
                    # a = 2*A = 2*k*u, b = k*w
                    pairs.add((2 * k * u, k * w))

                # Case 2: A = v, K = u
                denom2 = w + u
                num2 = v * w
                step2 = denom2 // math.gcd(num2, denom2)
                for k in range(step2, limit // w + 1, step2):
                    # a = 2*A = 2*k*v, b = k*w
                    pairs.add((2 * k * v, k * w))

    return len(pairs)

print(solve())
