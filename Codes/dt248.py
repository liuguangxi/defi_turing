from math import gcd

def solve():
    # Strategy that minimizes the maximum number of shots C(n) for a path graph.
    # For n >= 4, C(n) = 2n - 4. The sequence targets nodes: 2, 3, ..., n-1, n-1, n-2, ..., 2.
    n = 10
    if n == 1:
        s = [1]
    elif n == 2:
        s = [1, 1]
    elif n == 3:
        s = [2, 2]
    else:
        s = list(range(2, n)) + list(range(n - 1, 1, -1))

    # Use 0-based indexing for calculations.
    idx = [x - 1 for x in s]
    L = len(idx)

    # Dynamic Programming: W[k][j] stores the number of ways to finish a path of
    # length L starting from node j at step k.
    w = [[0] * n for _ in range(L + 1)]
    for j in range(n):
        w[L][j] = 1
    for k in range(L - 1, 0, -1):
        for j in range(n):
            if j > 0:
                w[k][j] += w[k + 1][j - 1]
            if j < n - 1:
                w[k][j] += w[k + 1][j + 1]

    # Total number of possible paths of length L.
    den = sum(w[1][j] for j in range(n))

    # DP to track number of paths not hit yet by the strategy.
    # active[j] is the number of partial paths of length k ending at j avoiding hits.
    active = [1 if j != idx[0] else 0 for j in range(n)]
    hit = [0] * L
    # H[0] is the number of paths starting at s[0] (which hit at step 1).
    hit[0] = w[1][idx[0]]

    for k in range(1, L):
        nxt = [0] * n
        for j in range(n):
            # Paths of length k+1 ending at j must come from neighbors at length k.
            ways = (active[j - 1] if j > 0 else 0) + (active[j + 1] if j < n - 1 else 0)
            if j == idx[k]:
                # Paths hitting for the first time at step k+1.
                hit[k] += ways * w[k + 1][j]
            else:
                # Paths that continue without being hit.
                nxt[j] = ways
        active = nxt

    # E(n) = sum(k * Count(hit_at_k)) / total_paths.
    num = sum((k + 1) * c for k, c in enumerate(hit))
    g = gcd(num, den)

    # Output the product of numerator and denominator of the irreducible fraction.
    print(f"E({n}) = {num // g}/{den // g}")
    return (num // g) * (den // g)

print(solve())
