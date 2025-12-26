import math

def solve():
    # The total number of digits in n and n^2 must be 9.
    # Since n is an integer, let d be the number of digits of n.
    # The number of digits of n^2 is either 2d or 2d-1.
    # So d + 2d = 9 or d + 2d - 1 = 9.
    # 3d = 9 => d = 3.
    # Therefore, n must be a 3-digit number.

    # We iterate through all 3-digit numbers starting from the smallest
    # n whose square has 6 digits (317^2 = 100489) up to 999.
    target_digits = set("123456789")

    for n in range(317, 1000):
        if n == 567:
            continue

        n_sq = n * n
        combined = str(n) + str(n_sq)

        # Check if the combined string has length 9 and contains digits 1-9 once
        if len(combined) == 9 and set(combined) == target_digits:
            return n

print(solve())
