import math

def find_nth_prime(n):
    if n == 1: return 2

    # Estimate the upper bound for the n-th prime
    # Using the formula: p_n < n(log n + log log n) for n >= 6
    limit = int(n * (math.log(n) + math.log(math.log(n)))) if n >= 6 else 15

    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    prime_count = 0
    for p in range(2, limit + 1):
        if sieve[p]:
            prime_count += 1
            if prime_count == n:
                return p
            # Mark multiples of p as not prime
            for i in range(p * p, limit + 1, p):
                sieve[i] = False

target_index = 23456
result = find_nth_prime(target_index)
print(result)
