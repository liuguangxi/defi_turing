def solve():
    """
    Finds the count of natural numbers n <= 10^13 such that the sum of
    digits of n is a perfect square.

    The maximum possible sum of digits for a number less than 10^13 is
    for 9,999,999,999,999, which is 13 * 9 = 117.
    The perfect squares up to 117 are: 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100.
    """
    # Max number of digits to consider (for numbers up to 10^13 - 1)
    num_digits = 13
    # Max possible sum of digits for 13 digits
    max_sum = 117

    # dp[i][s] will store the number of ways to have a sum of digits 's'
    # using 'i' digits (including leading zeros).
    dp = [[0] * (max_sum + 1) for _ in range(num_digits + 1)]
    dp[0][0] = 1

    for i in range(1, num_digits + 1):
        for s in range(max_sum + 1):
            # To get a sum 's' with 'i' digits, we take a sum 's-d' with 'i-1'
            # digits and append digit 'd' (0-9).
            for d in range(10):
                if s >= d:
                    dp[i][s] += dp[i-1][s-d]

    # Perfect squares within the range [0, 117]
    squares = [k*k for k in range(11) if k*k <= max_sum]

    # Sum of numbers in the range [0, 10^13 - 1] with square digit sums
    count_to_limit_minus_one = sum(dp[num_digits][sq] for sq in squares)

    return count_to_limit_minus_one + 1

print(solve())
