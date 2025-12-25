def solve():
    limit = 100_000
    # Sieve of Eratosthenes
    primes = [True] * limit
    primes[0] = primes[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            for j in range(i*i, limit, i):
                primes[j] = False

    # Store primes in a set for O(1) lookup
    prime_set = {i for i, is_p in enumerate(primes) if is_p}

    def is_circular(p):
        s = str(p)
        # Any multi-digit circular prime cannot contain 0, 2, 4, 5, 6, 8
        if len(s) > 1:
            for digit in '024568':
                if digit in s:
                    return False

        # Check all rotations
        for i in range(1, len(s)):
            rotation = int(s[i:] + s[:i])
            if rotation not in prime_set:
                return False
        return True

    count = 0
    for p in prime_set:
        if is_circular(p):
            count += 1

    return count

print(solve())
