import math

def solve():
    limit = 100000
    # Sieve of Eratosthenes to find primes up to limit
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False

    primes = [p for p, alive in enumerate(is_prime) if alive]

    contradictions_sum = 0
    # The problem asks for numbers between 2 and 100,000 (exclusive)
    # Check every odd number n in the range
    for n in range(3, limit, 2):
        found = False
        # The conjecture is n = p + 2 * k^2 where k >= 0
        k = 0
        while 2 * k * k < n:
            remainder = n - 2 * k * k
            if is_prime[remainder]:
                found = True
                break
            k += 1

        if not found:
            contradictions_sum += n

    return contradictions_sum

print(solve())
