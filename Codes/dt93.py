def solve():
    # We estimate the limit. Based on the growth of partitions,
    # n=200 is more than enough.
    limit = 200

    # Sieve of Eratosthenes to find all prime numbers up to limit
    is_prime = [True] * (limit + 1)
    primes = []
    for p in range(2, limit + 1):
        if is_prime[p]:
            primes.append(p)
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False

    # dp[i] will store the number of ways to write i as a sum of primes
    # We use the generating function approach for partitions into primes
    dp = [0] * (limit + 1)
    dp[0] = 1 # Base case: one way to make the sum 0

    # For each prime, update the possible ways to form each integer
    for p in primes:
        for i in range(p, limit + 1):
            dp[i] += dp[i - p]

    # Find the smallest integer n such that dp[n] > 1,000,000
    for n in range(1, limit + 1):
        if dp[n] > 1000000:
            return n

print(solve())
