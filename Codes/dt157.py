import math

def solve():
    n = 200
    seen_primitives = set()
    # From the condition that the circumradii of ABD and ADC are equal,
    # we find that triangle ABC must be isosceles with AB = AC.
    # Let h be the height of A above BC. D is on BC, BD = a, DC = b, DA = c.
    # By Stewart's Theorem or coordinate geometry: c^2 = AB^2 - ab.
    # The height h is sqrt(c^2 - ((a-b)/2)^2).
    # For the area S = (a+b)h/2 to be an integer, 4c^2 - (a-b)^2 must be a perfect square.
    # Let a-b = 2u and h = v. Then u^2 + v^2 = c^2 must form an integer Pythagorean triple.
    # a and b must have the same parity (since a-b = 2u).
    # Then S = (a+b)v/2 is an integer because a+b is even.

    # We count unique configurations (a, b, c) up to homothety (proportionality).
    # This is equivalent to counting primitive integer triples with gcd(a, b, c) = 1.
    for u in range(1, (n // 2) + 1):
        for c in range(u + 1, n + 1):
            v2 = c**2 - u**2
            v = int(math.isqrt(v2))
            if v * v == v2:
                # a - b = 2u => a = b + 2u
                # Constraints: 1 <= b < a <= 200 and c <= 200
                for b in range(1, n - 2 * u + 1):
                    a = b + 2 * u
                    if math.gcd(a, math.gcd(b, c)) == 1:
                        seen_primitives.add((a, b, c))
    return len(seen_primitives)

print(solve())
