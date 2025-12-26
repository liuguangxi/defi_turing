def solve():
    # Set a reasonable limit to search for n
    limit = 1000000
    phi = list(range(limit + 1))

    # Sieve to compute Euler's totient function values
    for i in range(2, limit + 1):
        if phi[i] == i:  # i is prime
            for j in range(i, limit + 1, i):
                phi[j] -= phi[j] // i

    # Search for the smallest n such that phi(n) == phi(n+1) == phi(n+2)
    for n in range(1, limit - 1):
        if phi[n] == phi[n+1] == phi[n+2]:
            return n

print(solve())
