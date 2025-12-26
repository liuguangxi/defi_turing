import itertools

def solve():
    # Number of digits in A is 4, in B is 2.
    # Configuration from image:
    # Row 3 (P1 = A * B_units) has 5 dots.
    # Row 4 (P2 = A * B_tens) has 4 dots.
    # Row 5 (Product = A * B) has 5 dots.

    solutions = []
    # a: 4 digits, so 1000 to 9999
    for a in range(1000, 10000):
        # b_tens: 1 to 9 (multiplier is 2 digits)
        for b_tens in range(1, 10):
            p2 = a * b_tens
            # Row 4 has 4 dots
            if not (1000 <= p2 <= 9999):
                continue

            # b_units: 1 to 9 (P1 must have 5 dots)
            for b_units in range(1, 10):
                p1 = a * b_units
                # Row 3 has 5 dots
                if not (10000 <= p1 <= 99999):
                    continue

                b = 10 * b_tens + b_units
                res = a * b
                # Row 5 has 5 dots
                if not (10000 <= res <= 99999):
                    continue

                # Check the number of distinct digits used in the whole multiplication
                all_digits = set(str(a)) | set(str(b)) | set(str(p1)) | set(str(p2)) | set(str(res))

                # Condition: exactly 4 distinct digits and no 2 or 3 digit solutions possible
                if len(all_digits) == 4:
                    solutions.append(res)

    # The problem asks for the product of the results of these two multiplications
    if len(solutions) == 2:
        return solutions[0] * solutions[1]
    return None

print(solve())
