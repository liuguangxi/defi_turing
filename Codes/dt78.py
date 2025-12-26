def solve():
    # Iterate through all 4-digit numbers abcd
    for a in range(1, 10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    n = 1000 * a + 100 * b + 10 * c + d
                    # The property is n = a^b * c^d
                    # Note: Python's 0**0 evaluates to 1
                    if (a**b) * (c**d) == n:
                        return n

print(solve())
