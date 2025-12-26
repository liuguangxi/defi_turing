def solve():
    target = 5000000
    best_diff = float('inf')
    best_area = 0

    # R(m, n) = (m*(m+1)/2) * (n*(n+1)/2)
    # We iterate m and find the best n
    # Max value for m is around sqrt(2 * target) when n=1
    limit = int((2 * target)**0.5) + 100

    for m in range(1, limit):
        m_factor = m * (m + 1) // 2

        # We want m_factor * (n*(n+1)/2) approx target
        # So n*(n+1)/2 approx target / m_factor
        n_target_factor = target / m_factor

        # Solve n^2 + n - 2*n_target_factor = 0
        # n = (-1 + sqrt(1 + 8*n_target_factor)) / 2
        n_approx = int((-1 + (1 + 8 * n_target_factor)**0.5) / 2)

        # Check n_approx and n_approx + 1
        for n in [n_approx, n_approx + 1]:
            if n <= 0:
                continue

            rect_count = m_factor * (n * (n + 1) // 2)
            diff = abs(rect_count - target)

            if diff < best_diff:
                best_diff = diff
                best_area = m * n
            elif diff == best_diff:
                # If tied, usually the problem implies a unique solution,
                # but we could track it.
                pass

    return best_area

print(solve())
