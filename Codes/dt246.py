def solve():
    # Let the points on the graph be (x_0, y_0), (x_1, y_1), ..., (x_{k-1}, y_{k-1}).
    # Let dx_i = x_i - x_{i-1} and dy_i = y_i - y_{i-1} for i = 1 to k-1.
    # Strictly increasing requires dx_i >= 1 and dy_i >= 1.
    # Strictly convex requires dy_1/dx_1 < dy_2/dx_2 < ... < dy_{k-1}/dx_{k-1}.
    # This implies that all rational slopes dy_i/dx_i must be distinct.
    # To maximize k in an N x N square, we choose segments with primitive vectors
    # (gcd(dx, dy) = 1) that minimize the cumulative sum of dx and dy.
    # By symmetry, the optimal set of segments involves choosing primitive vectors
    # with the smallest possible sum s = dx + dy first.

    N = 10**18

    # Estimate the range of s using the asymptote k ~ 3/pi^(2/3) * N^(2/3).
    # For N = 10^18, k_max ~ 1.4 * 10^12. The number of such vectors is roughly
    # the sum of phi(s) up to s_max. s_max ~ 2.15 * 10^6.
    limit = int(2.5 * (N * 10)**(1/3))
    phi = list(range(limit + 1))
    for i in range(2, limit + 1):
        if phi[i] == i:
            for j in range(i, limit + 1, i):
                phi[j] -= phi[j] // i

    a_sum = 0
    m_sum = 0
    k_max = 1
    # Collect all primitive vectors with sum s <= k_max.
    # For s > 1, the sum of dx for all dx < s with gcd(dx, s) = 1 is s * phi(s) / 2.
    for s in range(2, limit + 1):
        term = s * phi[s] // 2
        if a_sum + term <= N:
            a_sum += term
            m_sum += phi[s]
            k_max = s
        else:
            break

    # Remaining budget for both x and y dimensions.
    r = N - a_sum
    # Initial node count is segments + 1.
    count = m_sum + 1

    # Greedy-fill the remaining budget with segments from s = k_max + 1 onwards.
    # Pairs of vectors (dx, s-dx) and (s-dx, dx) are most efficient (cost s each).
    for s in range(k_max + 1, limit + 1):
        num_pairs_available = phi[s] // 2
        num_pairs_picked = min(num_pairs_available, r // s)
        count += 2 * num_pairs_picked
        r -= s * num_pairs_picked

        # If we can't fit another pair, check if we can fit one more balanced vector.
        if num_pairs_picked < num_pairs_available:
            # The most balanced vector for a given s has max(dx, dy) = ceil(s/2).
            if (s + 1) // 2 <= r:
                count += 1
            break

    return count

print(solve())
