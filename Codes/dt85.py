def solve():
    def permutations(n, k):
        res = 1
        for i in range(k):
            res *= (n - i)
        return res

    def sum_distinct_digits(k):
        if k == 1:
            return sum(range(1, 10))

        # Sum of lead digits (10^(k-1) position)
        # 9 options for lead digit (1-9), other (k-1) positions filled by remaining digits
        lead_sum = 10**(k-1) * sum(range(1, 10)) * permutations(9, k-1)

        # Sum of digits in other positions (10^0 to 10^(k-2))
        # For a fixed non-zero digit at position i:
        # lead digit has 8 options (1-9 excluding the fixed digit),
        # remaining k-2 positions have P(8, k-2) options.
        other_pos_sum = 0
        ways_per_digit = 8 * permutations(8, k-2)
        for i in range(k-1):
            other_pos_sum += 10**i * sum(range(1, 10)) * ways_per_digit

        return lead_sum + other_pos_sum

    # Range 1 to 100,000 covers 1, 2, 3, 4, and 5-digit numbers
    return sum(sum_distinct_digits(k) for k in range(1, 6))

print(solve())
