def solve():
    # Grid size
    m = 100 * 100
    # Probability of all darts hitting distinct squares
    prob_distinct = 1.0
    n = 0

    # We want the smallest n such that 1 - prob_distinct > 0.5, i.e., prob_distinct < 0.5
    while prob_distinct >= 0.5:
        # Increment dart count
        n += 1
        # Probability that the n-th dart hits a square not yet hit
        # Note: the (n-1)-th dart was already processed in the previous iteration
        prob_distinct *= (m - (n - 1)) / m

    return n

print(solve())
