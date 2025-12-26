def solve():
    # We want to find the largest N (with 7 digits) such that
    # the count of numbers from 1 to N containing at least one '5' is exactly N/2.

    # N is a 7-digit positive integer, so 1,000,000 <= N <= 9,999,999.
    # However, we can start checking from N=1 upwards and keep track of the largest.
    count_with_5 = 0
    max_n = -1

    # Iterate through all positive integers up to the maximum 7-digit number.
    for n in range(1, 10000000):
        # A number contains a 5 if '5' is in its string representation.
        if '5' in str(n):
            count_with_5 += 1

        # Check if the condition count_with_5 == n/2 is satisfied.
        if 2 * count_with_5 == n:
            max_n = n

    return max_n

print(solve())
