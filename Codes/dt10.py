def sum_primes_up_to(limit):
    """Calculates the sum of all primes <= limit using the Sieve of Eratosthenes."""
    if limit < 2:
        return 0

    # Create a boolean array for the sieve
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    # Sieve of Eratosthenes
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            # Mark multiples of p starting from p*p
            for i in range(p * p, limit + 1, p):
                sieve[i] = False

    # Sum all prime indices
    return sum(p for p, is_prime in enumerate(sieve) if is_prime)

limit = 10_000_000
result = sum_primes_up_to(limit)
print(result)
