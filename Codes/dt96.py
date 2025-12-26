import math

def solve():
    limit = 1000000000

    # Sieve to find all primes up to sqrt(limit)
    sqrt_limit = int(math.sqrt(limit)) + 1
    is_prime = [True] * (sqrt_limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(sqrt_limit)) + 1):
        if is_prime[i]:
            for j in range(i*i, sqrt_limit + 1, i):
                is_prime[j] = False

    primes = [i for i, val in enumerate(is_prime) if val]

    # Lists of prime powers
    r4_vals = [p**4 for p in primes if p**4 < limit]
    q3_vals = [p**3 for p in primes if p**3 < limit]
    p2_vals = [p**2 for p in primes if p**2 < limit]

    # Use chunking to manage memory efficiently (approx 200MB per chunk)
    total_count = 0
    chunk_size = 200_000_000

    for chunk_start in range(0, limit + 1, chunk_size):
        chunk_end = min(chunk_start + chunk_size, limit + 1)
        seen = bytearray(chunk_end - chunk_start)

        for r4 in r4_vals:
            if r4 >= chunk_end:
                break
            for q3 in q3_vals:
                r4q3 = r4 + q3
                if r4q3 >= chunk_end:
                    break

                # Check each p2. Optimization: only iterate p2 that could fall in this chunk
                for p2 in p2_vals:
                    val = r4q3 + p2
                    if val >= chunk_end:
                        break
                    if val >= chunk_start:
                        seen[val - chunk_start] = 1

        # count() is faster than sum() for bytearray
        total_count += seen.count(1)

    return total_count

print(solve())
