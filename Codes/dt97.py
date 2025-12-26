def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return n % 2 != 0

def check_pattern(n, pattern):
    s = str(n)
    if len(s) != len(pattern):
        return False
    for char, digit in zip(pattern, s):
        d = int(digit)
        if char == 'I' and not is_odd(d):
            return False
        if char == 'P' and not is_even(d):
            return False
    return True

def solve():
    evens = [0, 2, 4, 6, 8]
    odds = [1, 3, 5, 7, 9]

    # Generate N1: format I P P
    for d1 in odds:
        for d2 in evens:
            for d3 in evens:
                n1 = 100 * d1 + 10 * d2 + d3

                # Generate d4 and d5 (multiplier digits): P P
                for d5 in evens: # Multiplier second digit
                    # Row 1: n1 * d5 must be format P I P P
                    row1 = n1 * d5
                    if not check_pattern(row1, "PIPP"):
                        continue

                    for d4 in [2, 4, 6, 8]: # Multiplier first digit (cannot be zero)
                        # Row 2: n1 * d4 must be format P I P
                        row2 = n1 * d4
                        if not check_pattern(row2, "PIP"):
                            continue

                        # Final product: (n1 * d5) + (n1 * d4 * 10) must be format I I P P
                        product = row1 + 10 * row2
                        if check_pattern(product, "IIPP"):
                            return product

print(solve())
