import math

def solve():
    """
    Solves the maximum quadrilateral area problem.
    The function F(a, b, p) calculates the maximum area of a quadrilateral
    with diagonals a, b and perimeter p.
    For the given range 1000 <= b < a <= 1200 and 2400 < p <= 2800,
    the perimeter p is always less than 2 * sqrt(a^2 + b^2).
    In this case, the maximum area is achieved when the diagonals intersect
    at their midpoints, and is given by F(a, b, p) = sqrt((p^2 - 4a^2)(p^2 - 4b^2)) / 8.
    For F to be an integer, p must be even because if p is odd, the term
    (p^2 - 4a^2)(p^2 - 4b^2) is odd, and its square root is odd, so it cannot
    be divisible by 8.
    """
    areas = set()

    # Iterate through even perimeters in the range (2400, 2800]
    for p in range(2402, 2801, 2):
        k = p // 2
        k2 = k * k

        # Iterate through diagonal 'a' in the range [1001, 1200]
        # p > 2a must hold, so a < k
        for a in range(1001, min(1201, k)):
            k2_minus_a2 = k2 - a * a

            # Precompute GCD of a and p to optimize the inner loop
            gap = math.gcd(a, p)

            # Iterate through diagonal 'b' in the range [1000, a-1]
            for b in range(1000, a):
                # Condition GCD(a, b, p) = 1
                if math.gcd(gap, b) == 1:
                    k2_minus_b2 = k2 - b * b

                    # Compute F(a, b, p) = 0.5 * sqrt((k^2 - a^2)(k^2 - b^2))
                    val = k2_minus_a2 * k2_minus_b2
                    root = math.isqrt(val)

                    # Check if the expression inside the square root is a perfect square
                    if root * root == val:
                        # Area = root / 2 must be an integer
                        if root % 2 == 0:
                            areas.add(root // 2)

    # Return the sum of all distinct integer values found
    return sum(areas)

print(solve())
