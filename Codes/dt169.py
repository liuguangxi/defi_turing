import math

def nCr(n, r):
    if r < 0 or r > n:
        return 0
    return math.comb(n, r)

def reduced_menage(n):
    total = 0
    for k in range(n + 1):
        term = ((-1)**k) * (2*n / (2*n - k)) * nCr(2*n - k, k) * math.factorial(n - k)
        total += int(term)
    return total

n = 11
Mn = reduced_menage(n)
total_labeled = 2 * math.factorial(n) * Mn
print(total_labeled)
