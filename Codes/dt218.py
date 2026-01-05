def solve_turing_2017():
    """
    Finds the number of integers n between 1 and 10^10 such that the square root
    of n has '2017' as the first digits after the decimal point.

    Condition: I + 0.2017 <= sqrt(n) < I + 0.2018
    This translates to: (I + 0.2017)^2 <= n < (I + 0.2018)^2
    We can rewrite this using integer arithmetic to maintain precision:
    (10000*I + 2017)^2 / 10^8 <= n < (10000*I + 2018)^2 / 10^8
    """
    limit = 10**10
    total_count = 0

    # Since sqrt(n) <= 100,000, the integer part I can range from 0 to 99,999.
    # If I = 100,000, sqrt(n) >= 100000.2017, so n > 10^10.
    for i in range(100000):
        # Calculate the lower and upper bounds for n at integer part i
        low_sq = (10000 * i + 2017) ** 2
        high_sq = (10000 * i + 2018) ** 2

        # Calculate the first and last candidate integers n in the interval.
        # ceil(low_sq / 10^8)
        first_n = (low_sq + 10**8 - 1) // 10**8
        # floor((high_sq - 1) / 10^8)
        last_n = (high_sq - 1) // 10**8

        # We only consider n <= 10^10
        if first_n > limit:
            break

        effective_last = min(last_n, limit)

        # Count the integers in the range [first_n, effective_last]
        if effective_last >= first_n:
            total_count += (effective_last - first_n + 1)

    return total_count

# Printing the result as the solution to the problem
print(solve_turing_2017())
