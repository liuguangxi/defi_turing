import math

def get_primes(n):
    """Sieve of Eratosthenes to find all primes up to n."""
    primes = []
    is_prime = [True] * (n + 1)
    for p in range(2, n + 1):
        if is_prime[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
    return primes

def get_prime_factors(n):
    """Returns the set of prime factors of n."""
    factors = set()
    d = 2
    temp = n
    while d * d <= temp:
        if temp % d == 0:
            factors.add(d)
            while temp % d == 0:
                temp //= d
        d += 1
    if temp > 1:
        factors.add(temp)
    return factors

def is_long_prime(p):
    """
    Checks if a prime p is a long (full-reptend) prime in base 10.
    A prime p is long if the order of 10 modulo p is p - 1.
    """
    if p == 2 or p == 5:
        return False
    phi = p - 1
    factors = get_prime_factors(phi)
    for q in factors:
        if pow(10, phi // q, p) == 1:
            return False
    return True

def solve():
    """
    Finds the last 10 digits of the sum of all cyclic numbers with at
    most 5000 digits. A cyclic number of length L corresponds to the
    period of a long prime p where L = p - 1.
    """
    MOD = 10**10
    limit = 5000

    # Cyclic numbers with length L <= 5000 imply p - 1 <= 5000, so p <= 5001.
    primes = get_primes(limit + 1)
    long_primes = [p for p in primes if is_long_prime(p)]

    total_sum_mod = 0
    for p in long_primes:
        length = p - 1
        # The cyclic number C_p is defined as (10^(p-1) - 1) / p.
        if length < 10:
            # For small lengths, calculate the value directly.
            cyclic_number = (10**length - 1) // p
            total_sum_mod = (total_sum_mod + cyclic_number) % MOD
        else:
            # For lengths >= 10, 10^(p-1) is divisible by 10^10.
            # Thus, (10^(p-1) - 1) / p  = -1 / p (mod 10^10).
            # We calculate this using the modular inverse of p modulo 10^10.
            inv_p = pow(p, -1, MOD)
            val_mod = (MOD - inv_p) % MOD
            total_sum_mod = (total_sum_mod + val_mod) % MOD

    return f"{total_sum_mod:010d}"

print(solve())
