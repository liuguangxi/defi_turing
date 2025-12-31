import math

def sieve(limit):
    """Sieve of Eratosthenes to find primes up to a limit."""
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(limit**0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
    return is_prime, [p for p, val in enumerate(is_prime) if val]

def solve():
    """
    Finds the longest arithmetic sequence of prime numbers less than 1 million,
    given the first term is not 13 or 17, and returns the sum of its terms.
    """
    limit = 1000000
    is_prime, primes_list = sieve(limit)

    # For a prime arithmetic sequence of length k, the common difference d must
    # be a multiple of the primorial P(k), unless the sequence starts at k.
    # For length k=13, since the first term is not 13, d must be a multiple of
    # P(13) = 2*3*5*7*11*13 = 30030.

    best_len = 0
    best_sum = 0

    # Searching from k=15 downwards as the longest likely length in this range.
    for k in range(15, 10, -1):
        # For k >= 13, d must be a multiple of 30030.
        # For k = 11, 12, d would be a multiple of 2310.
        step = 30030 if k >= 13 else 2310

        for d in range(step, limit // (k-1) + 1, step):
            for a in primes_list:
                # First term constraint
                if a == 13 or a == 17:
                    continue
                # Ensure the last term of the checked length is within bounds
                if a + (k-1)*d >= limit:
                    break

                # Check primality of all terms in the sequence
                is_valid = True
                for i in range(1, k):
                    if not is_prime[a + i * d]:
                        is_valid = False
                        break

                if is_valid:
                    # Count actual length by checking further extensions
                    curr_len = k
                    current_term = a + k * d
                    while current_term < limit and is_prime[current_term]:
                        curr_len += 1
                        current_term += d

                    if curr_len > best_len:
                        best_len = curr_len
                        best_sum = sum(a + i * d for i in range(curr_len))

        # If we found sequences for a specific k, we stop as we search downwards.
        if best_len > 0:
            break

    return best_sum

print(solve())
