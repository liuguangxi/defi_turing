import math

def solve():
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    target_index = 2_000_000 - 1  # 0-based index
    permutation = ""

    for i in range(9, -1, -1):
        fact = math.factorial(i)
        # Determine which digit block the index falls into
        digit_idx = target_index // fact
        # Append the digit and remove it from the available pool
        permutation += str(digits.pop(digit_idx))
        # Update index for the next digit
        target_index %= fact

    return permutation

print(solve())
