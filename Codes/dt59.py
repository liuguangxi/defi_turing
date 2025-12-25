def sum_proper_divisors(n):
    if n < 2: return 0
    total = 1
    d = 2
    temp = n
    while d * d <= temp:
        if temp % d == 0:
            p_sum = 1
            p_pow = 1
            while temp % d == 0:
                p_pow *= d
                p_sum += p_pow
                temp //= d
            total *= p_sum
        d += 1
    if temp > 1:
        total *= (1 + temp)
    return total - n

def solve():
    limit_k = 666
    p = {}
    # We check n up to a safe bound.
    # For k < 666, if n is not prime or p*q, it must be small.
    # If n = p^2, n < 665^2 = 442225.
    # If n = p*q, n is maximized when p=2, but that gives small k.
    # The largest n such that s_p_d(n) < 666 will be around 665^2.
    max_n = 500000
    for n in range(1, max_n):
        k = sum_proper_divisors(n)
        if k < limit_k:
            if k not in p:
                p[k] = n
    return max(p.values())

print(solve())
