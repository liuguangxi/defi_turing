def solve():
    N = 10**6
    spf = [0] * (N + 1)
    primes = []
    pi = [0] * (N + 1)

    for i in range(2, N + 1):
        if spf[i] == 0:
            spf[i] = i
            primes.append(i)
        pi[i] = len(primes)
        for p in primes:
            if p > spf[i] or i * p > N:
                break
            spf[i * p] = p

    ans = sum(pi[spf[i]] for i in range(2, N + 1))
    return ans

print(solve())
