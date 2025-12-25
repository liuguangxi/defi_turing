def get_divisor_sums(limit):
    # Sieve-like approach to find sum of proper divisors for all n up to limit
    sums = [1] * (limit + 1)
    sums[0] = 0
    sums[1] = 0
    for i in range(2, int(limit**0.5) + 1):
        # Every multiple j of i has i as a divisor
        # i*i is the start to avoid double counting, but we can't do that easily
        # for simple addition. We'll use a standard sieve.
        pass

    # Correct sieve approach:
    divisor_sums = [0] * (limit + 1)
    for i in range(1, limit // 2 + 1):
        for j in range(2 * i, limit + 1, i):
            divisor_sums[j] += i
    return divisor_sums

def solve():
    limit = 100_000
    d = get_divisor_sums(limit)

    amicable_sum = 0
    for a in range(1, limit + 1):
        b = d[a]
        # Check if b is within bounds to use precomputed d[b]
        # If b is out of bounds, we calculate d(b) on the fly
        if b > 1 and a != b:
            if b <= limit:
                val_b = d[b]
            else:
                # Calculate d(b) manually
                val_b = 1
                for i in range(2, int(b**0.5) + 1):
                    if b % i == 0:
                        val_b += i
                        if i*i != b:
                            val_b += b // i

            if val_b == a:
                amicable_sum += a

    return amicable_sum

print(solve())
