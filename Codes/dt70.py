def solve():
    # A 6-digit number N can be written as 10*X + d0
    # Moving d0 to the left gives N' = d0 * 10^5 + X
    # We are given N' = k * N for some integer k > 1
    # d0 * 10^5 + X = k * (10 * X + d0)
    # d0 * (10^5 - k) = X * (10 * k - 1)
    # X = d0 * (10^5 - k) / (10 * k - 1)

    solutions = []
    # k can range from 2 to 9 (since N and N' are 6-digit numbers)
    for k in range(2, 10):
        for d0 in range(1, 10):
            numerator = d0 * (10**5 - k)
            denominator = 10 * k - 1
            if numerator % denominator == 0:
                X = numerator // denominator
                # N must be a 6-digit number, so X must be 5 digits (can have leading zeros if N doesn't)
                # but the number N = 10*X + d0 must be between 100,000 and 999,999.
                n = 10 * X + d0
                if 100000 <= n <= 999999:
                    # Verify the property: move last digit to front
                    s_n = str(n)
                    n_prime = int(s_n[-1] + s_n[:-1])
                    if n_prime == k * n:
                        solutions.append(n)

    # Sum of unique 6-digit numbers
    return sum(set(solutions))

print(solve())
