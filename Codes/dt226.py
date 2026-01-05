import math

def get_ep(p, max_val):
    """
    Calculates the exponent e_p of a prime p in the product
    n = 3! * 5! * 7! * ... * 4999!.
    e_p = sum_{j=1}^{2499} v_p((2j+1)!)
    Using Legendre's formula logic: e_p = sum_{k>=1} sum_{j=1}^{2499} floor((2j+1)/p^k)
    """
    e_p = 0
    pk = p
    while pk <= max_val:
        m = 1
        while m * pk <= max_val:
            # We need to find how many odd numbers x in {3, 5, ..., 4999}
            # satisfy x >= m * pk.
            # Let x = 2j+1. Then 2j+1 >= m * pk  => 2j >= m*pk - 1.
            # The smallest such j is ceil((m*pk - 1)/2), which is equivalent
            # to (m * pk) // 2 in integer arithmetic.
            j_min = (m * pk) // 2
            start_j = max(1, j_min)
            if start_j <= 2499:
                # The range of j is [start_j, 2499].
                e_p += (2499 - start_j + 1)
            else:
                break
            m += 1
        pk *= p
    return e_p

def solve():
    # Sieve of Eratosthenes to find all primes up to 4999
    limit = 5000
    is_prime = [True] * (limit + 1)
    primes = []
    for p in range(2, limit + 1):
        if is_prime[p]:
            primes.append(p)
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False

    # The number of cubic divisors is the product over all prime factors
    # of (floor(e_p/3) + 1).
    total_cubes = 1
    for p in primes:
        ep = get_ep(p, 4999)
        total_cubes *= (ep // 3 + 1)

    # The result requested is the twelve digits before the trailing zeros
    # of the total count of cubes.
    s = str(total_cubes).rstrip('0')
    return s[-12:]

print(solve())
