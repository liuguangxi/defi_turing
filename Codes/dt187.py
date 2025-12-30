import math

def get_period_digits(num, den):
    """Calculates the repeating part of the decimal expansion of num/den."""
    # Track remainders to find the start and end of the repeating cycle
    remainders = []
    digits = []
    curr_rem = num % den

    while curr_rem not in remainders:
        remainders.append(curr_rem)
        curr_rem *= 10
        digits.append(curr_rem // den)
        curr_rem %= den

        # If remainder becomes 0, there is no repeating part
        if curr_rem == 0:
            return ""

    # The cycle starts at the index where the remainder was first seen
    start_idx = remainders.index(curr_rem)
    return "".join(map(str, digits[start_idx:]))

# 1. Define range
N = 10000

# 2. Calculate the total number of ways to pick two distinct integers
# Total = C(10000, 2)
total_pairs = N * (N - 1) // 2

# 3. Calculate the number of favorable pairs (a, b) where a < b and b % a == 0
# For each 'a', there are floor(N/a) - 1 such 'b's.
favorable_pairs = sum(N // a for a in range(1, N + 1)) - N

# 4. Simplify the probability fraction
common = math.gcd(favorable_pairs, total_pairs)
num = favorable_pairs // common
den = total_pairs // common

# 5. Extract the repeating decimal digits (the period)
print(get_period_digits(num, den))
