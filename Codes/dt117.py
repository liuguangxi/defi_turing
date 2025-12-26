def count_almost_primes(limit):
    # Sieve to find all primes up to limit/2
    sieve_limit = limit // 2
    sieve = [True] * (sieve_limit + 1)
    sieve[0] = sieve[1] = False
    for p in range(2, int(sieve_limit**0.5) + 1):
        if sieve[p]:
            for i in range(p * p, sieve_limit + 1, p):
                sieve[i] = False

    primes = [p for p, is_p in enumerate(sieve) if is_p]

    count = 0
    num_primes = len(primes)
    # Iterate through distinct pairs (p, q) such that p < q and p * q < limit
    for i in range(num_primes):
        p = primes[i]
        # If p*p >= limit, no more pairs (p, q) with p < q exist
        if p * p >= limit:
            break
        for j in range(i + 1, num_primes):
            if p * primes[j] < limit:
                count += 1
            else:
                break
    return count

print(count_almost_primes(100000))
