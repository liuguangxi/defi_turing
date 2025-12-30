import collections

def is_valid_line(n, length, allowed_seven_indices):
    """
    Checks if a number n has a specific decimal representation.
    - length: the required number of digits.
    - allowed_seven_indices: indices (0-based) where the digit '7' is allowed (and required).
    - all other indices must not contain the digit '7'.
    """
    s = str(n)
    if len(s) != length:
        return False
    for i, char in enumerate(s):
        if char == '7':
            if i not in allowed_seven_indices:
                return False
        else:
            if i in allowed_seven_indices:
                return False
    return True

def solve():
    """
    Solves the French long division cryptarithm puzzle:
    _ 7 _ _ 7 _ |    _ 7
      _ _       | _ _ _ _ _
        7 _     |
        _ _ 7   |
            _ _ |
              0 |
    """
    valid_dividends = set()

    # Iterate through possible divisors d = [ds, 7]
    for ds in range(1, 10):
        d = ds * 10 + 7
        # Divisor pattern: _ 7
        if not is_valid_line(d, 2, {1}):
            continue

        # We need to find Dividend D = [D1, 7, D3, D4, 7, D6]
        # and Quotient Q = [q1, q2, q3, q4, q5]
        # such that D = d * Q

        # Iterate through possible digits for the dividend
        # D1 (pos 0) must be 1-9 to be a 6-digit number
        for D1 in range(1, 10):
            for D3 in range(10):
                for D4 in range(10):
                    for D6 in range(10):
                        D = D1*100000 + 70000 + D3*1000 + D4*100 + 70 + D6

                        # Dividend must be exactly divisible by d
                        if D % d != 0:
                            continue

                        # Dividend pattern: _ 7 _ _ 7 _
                        if not is_valid_line(D, 6, {1, 4}):
                            continue

                        # Quotient must be 5 digits (due to blanks) and have no 7s
                        Q = D // d
                        if not is_valid_line(Q, 5, set()):
                            continue

                        # Trace the "short" French division steps (remainders only)
                        # Step 1: Use first two digits (D1, 7)
                        r1 = (D1 * 10 + 7) % d
                        # Line 2: remainder + next digit (D3)
                        L2 = r1 * 10 + D3
                        # Pattern: _ _ (2 digits, no 7s)
                        if not is_valid_line(L2, 2, set()):
                            continue

                        # Step 2: Use Line 2
                        r2 = L2 % d
                        # Line 3: remainder + next digit (D4)
                        L3 = r2 * 10 + D4
                        # Pattern: 7 _ (2 digits, 7 at first pos)
                        if not is_valid_line(L3, 2, {0}):
                            continue

                        # Step 3: Use Line 3
                        r3 = L3 % d
                        # Line 4: remainder + next digit (7)
                        L4 = r3 * 10 + 7
                        # Pattern: _ _ 7 (3 digits, 7 at last pos)
                        if not is_valid_line(L4, 3, {2}):
                            continue

                        # Step 4: Use Line 4
                        r4 = L4 % d
                        # Line 5: remainder + next digit (D6)
                        L5 = r4 * 10 + D6
                        # Pattern: _ _ (2 digits, no 7s)
                        if not is_valid_line(L5, 2, set()):
                            continue

                        # Step 5: Final remainder must be 0
                        if L5 % d == 0:
                            valid_dividends.add(D)

    return sum(valid_dividends)

print(solve())
