import math
import itertools

def vp(p, n):
    """Exponent of prime p in the factorization of n!"""
    res = 0
    while n >= p:
        n //= p
        res += n
    return res

def Ep(p, n):
    """Exponent of prime p in the factorization of the product of factorials up to n!"""
    return sum(vp(p, i) for i in range(2, n + 1))

def solve():
    N = 99
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    # Represent the square-free part of i! as a bitmask of prime parities.
    v = [0] * (N + 1)
    current_parity = 0
    for i in range(2, N + 1):
        num = i
        for idx, p in enumerate(primes):
            count = 0
            while num % p == 0:
                count += 1
                num //= p
            if count % 2 == 1:
                current_parity ^= (1 << idx)
        v[i] = current_parity

    # The square-free part of the product of all factorials from 2! to 99!
    target = 0
    for i in range(2, N + 1):
        target ^= v[i]

    # Find the smallest subset S of {2..98} whose XOR sum matches 'target'.
    # Smallest size is known to be 4 for N=99.
    # To maximize P, minimize product of factorials in S.
    log_facs = [math.lgamma(i + 1) for i in range(N + 1)]
    best_S = None
    min_log_sum = float('inf')

    # Iterate through combinations of size 4.
    for combo in itertools.combinations(range(2, N), 4):
        res_xor = 0
        for idx in combo:
            res_xor ^= v[idx]
        if res_xor == target:
            log_sum = sum(log_facs[i] for i in combo)
            if log_sum < min_log_sum:
                min_log_sum = log_sum
                best_S = combo

    # Calculate prime exponents in P = (99! * 98! * ... * 2!) / (product s! for s in S).
    exponents = {}
    for p in primes:
        e = Ep(p, N) - sum(vp(p, s) for s in best_S)
        exponents[p] = e

    # Calculate trailing zeros k = min(e2, e5). Since e2 > e5, k = e5.
    k = exponents[5]
    mod = 10**10

    # Result = (P / 10^k) mod 10^10
    # P / 10^k = 2^(e2-k) * 5^(e5-k) * 3^e3 * ...
    # Since e5 = k, 5^(e5-k) = 1.
    ans = pow(2, exponents[2] - k, mod)
    for p in primes:
        if p == 2 or p == 5:
            continue
        ans = (ans * pow(p, exponents[p], mod)) % mod

    return f"{ans:010d}"

print(solve())
