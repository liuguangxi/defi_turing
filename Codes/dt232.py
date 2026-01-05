def solve():
    N = 10**6
    ans = 0
    # For a fixed k, we look for n = k*x such that x >= k and x has the same parity as k.
    # This ensures that n is the sum of k consecutive odd integers starting from a positive odd a.
    # The condition n = k(a + k - 1) implies a = n/k - k + 1.
    # For a to be an odd integer, n/k and k must have the same parity.
    # For a >= 1, we need n/k >= k.
    # Summing F(n) for n from 1 to N is equivalent to counting pairs (k, x)
    # such that 2 <= k, k <= x, x == k (mod 2), and k*x <= N.
    for k in range(2, int(N**0.5) + 1):
        M = N // k
        # Count x in {k, k+2, ..., M}
        count = (M - k) // 2 + 1
        ans += count
    return ans

print(solve())
