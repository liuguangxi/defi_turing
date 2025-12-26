import math

def solve():
    m = 10000
    results = []
    # Loop through all possible values of the second 4-digit block Y
    for y in range(m):
        # Discriminant for the quadratic X^2 - mX + (Y^2 - Y) = 0
        disc = m*m - 4*(y*y - y)
        if disc >= 0:
            sq = math.isqrt(disc)
            if sq * sq == disc:
                # Potential first 4-digit blocks X
                for x in [(m + sq) // 2, (m - sq) // 2]:
                    # Ensure the total number is exactly 8 digits
                    val = m * x + y
                    if 10000000 <= val <= 99999999:
                        results.append(val)
    return max(results) if results else None

print(solve())
