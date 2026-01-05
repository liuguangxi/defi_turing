import math

def solve():
    # Calculation of the Least Common Multiple (LCM) of all integers from 1 to 18.
    # An integer divisible by all integers less than 19 (1, 2, ..., 18)
    # must be a multiple of this LCM.
    lcm_val = 1
    for i in range(1, 19):
        lcm_val = (lcm_val * i) // math.gcd(lcm_val, i)

    total_sum = 0

    # A 10-pandigital integer consists of all 10 digits (0-9) exactly once.
    # Therefore, such an integer must have exactly 10 digits.
    # Standard decimal representation implies the first digit is non-zero.
    # Range of 10-digit integers is [1,000,000,000, 9,999,999,999].
    lower_bound = 10**9
    upper_bound = 10**10

    # Start at the first multiple of lcm_val that is at least 1,000,000,000.
    start_n = ((lower_bound + lcm_val - 1) // lcm_val) * lcm_val

    # Iterate through all multiples of the LCM within the 10-digit range.
    for n in range(start_n, upper_bound, lcm_val):
        s = str(n)
        # Check if the integer uses all 10 distinct digits.
        # Since n has 10 digits, if the set of its digits has size 10,
        # it must contain each digit from 0 to 9 exactly once.
        if len(set(s)) == 10:
            total_sum += n

    print(total_sum)

solve()
