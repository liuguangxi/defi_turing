def solve():
    limit = 1000000
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    n = 1
    for p in primes:
        if n * p >= limit:
            break
        n *= p
    return n

print(solve())
