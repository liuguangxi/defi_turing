import random

def is_prime(n):
    """Efficient primality test using Miller-Rabin for n < 3*10^18."""
    if n < 2: return False
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    # Deterministic bases for Miller-Rabin test for numbers up to the range
    # of the problem (less than 900 billion).
    for a in [2, 3, 5, 7, 11, 13, 17, 19, 23]:
        if n <= a: break
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def solve():
    # As derived, q must be 3 because if q > 3, p+q+1 would be a multiple of 3.
    # q=3 satisfies the conditions: q=3 (prime), q+4=7 (prime), q+10=13 (prime).
    # We then search for the largest p < 900,000,000,000 such that
    # p, p+6, p+10 are prime and p+q+1 = p+4 is prime.
    # This means p, p+4, p+6, p+10 must all be prime.
    limit = 900000000000

    # We search backwards from the limit.
    # Modular constraints: p must be 1 mod 3 and either 2 or 3 mod 5 (to avoid multiples of 3 or 5).
    # Combined with p being odd, p must be 7 mod 30 or 13 mod 30.
    for p in range(limit - 1, 0, -1):
        if p % 30 in [7, 13]:
            # Check the primality of the required values.
            if is_prime(p) and is_prime(p + 4) and is_prime(p + 6) and is_prime(p + 10):
                # q=3 is fixed, so p + q = p + 3.
                return p + 3
    return None

print(solve())
