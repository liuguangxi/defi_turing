import math

def solve():
    """
    F(n) is the smallest x such that x^2 is the sum of n consecutive
    positive integers starting from a >= 1.
    The sum S of n integers starting from a is:
    S = n * a + n * (n - 1) / 2 = (n / 2) * (2a + n - 1)
    Let x^2 = S.

    Condition for F(n) to exist:
    - If n is even, let n = 2^u * m (m odd).
      For x^2 = 2^(u-1) * m * (2a + n - 1) to be a square,
      v_2(x^2) = u - 1 must be even, so u must be odd.
    - If n is odd, F(n) always exists.

    Minimizing x:
    - If n is odd: x^2 = n * (a + (n-1)/2).
      Let j = a + (n-1)/2. Smallest j >= (n+1)/2 such that n*j is a square.
    - If n is even (u odd): x^2 = 2^(u-1) * m * (2a + n - 1).
      Let M = 2a + n - 1 (always odd). Smallest odd M >= n + 1
      such that m * M is a square.
    """
    limit = 1000000
    # Sieve to find Smallest Prime Factor (SPF)
    spf = list(range(limit + 1))
    for i in range(2, int(limit**0.5) + 1):
        if spf[i] == i:
            for j in range(i*i, limit + 1, i):
                if spf[j] == j:
                    spf[j] = i

    total_sum_f = 0

    for n in range(1, limit + 1):
        # Determine valuation of 2 and odd part m
        u = 0
        m = n
        while m % 2 == 0:
            u += 1
            m >>= 1

        # If n is even and v_2(n) is even, F(n) = 0
        if u > 0 and u % 2 == 0:
            continue

        # Compute the core (product of prime factors with odd exponents)
        # and s_odd (the root of the smallest square multiple of m)
        core_odd = 1
        s_odd = 1
        temp = m
        while temp > 1:
            p = spf[temp]
            cnt = 0
            while temp % p == 0:
                cnt += 1
                temp //= p
            if cnt % 2 != 0:
                core_odd *= p
            s_odd *= p**((cnt + 1) // 2)

        if u == 0: # Case: n is odd
            # Condition: j = c * k^2 >= (n+1)/2
            target = (n + 1) // 2
            k = math.isqrt(target // core_odd)
            if k * k * core_odd < target:
                k += 1
            total_sum_f += s_odd * k
        else: # Case: n is even and u is odd
            # x is a multiple of S = 2^((u-1)/2) * s_odd
            s = (1 << ((u - 1) // 2)) * s_odd
            # Condition: M = c * k^2 >= n + 1, where k must be odd
            target = n + 1
            k = math.isqrt(target // core_odd)
            if k * k * core_odd < target:
                k += 1
            if k % 2 == 0:
                k += 1
            total_sum_f += s * k

    return total_sum_f

print(solve())
