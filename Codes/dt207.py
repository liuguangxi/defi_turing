import math

def sieve(limit):
    """
    Returns a list of all prime numbers up to a specified limit
    using the Sieve of Eratosthenes.
    """
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for p in range(2, int(math.isqrt(limit)) + 1):
        if primes[p]:
            for i in range(p * p, limit + 1, p):
                primes[i] = False
    return [p for p, is_prime in enumerate(primes) if is_prime]

def solve():
    """
    Solves the regions problem by summing primes up to 10,000 that do not
    divide any term in the sequence R_n = n(n+1)/2 + 1.

    A prime p divides R_n if (n^2 + n + 2) / 2 is 0 mod p.
    For p = 2: R_1 = 2, so 2 divides an element.
    For p = 7: R_3 = 7, so 7 divides an element.
    For p > 2 and p != 7:
    n^2 + n + 2 ≡ 0 (mod p) has a solution if and only if the discriminant
    D = 1^2 - 4(1)(2) = -7 is a quadratic residue modulo p.
    The Legendre symbol (-7/p) equals (p/7) for all odd primes p.
    Thus, p does not divide any element R_n if and only if (p/7) = -1.
    The quadratic non-residues modulo 7 are {3, 5, 6}.
    """
    limit = 10000
    primes = sieve(limit)

    # We sum primes p <= 10,000 such that p mod 7 is in {3, 5, 6}.
    # Note: 2 and 7 are implicitly excluded as 2 % 7 = 2 and 7 % 7 = 0.
    total_sum = sum(p for p in primes if p % 7 in {3, 5, 6})

    return total_sum

# Standard execution of the solution
print(solve())
