import math

def solve():
    """
    Finds the sum of the first 14 terms of the strictly increasing sequence (u_n)
    where u_n is the smallest natural number such that no non-empty subset sum
    of {u_1, ..., u_n} is a perfect square.
    """

    def is_square(n):
        if n < 0: return False
        return math.isqrt(n)**2 == n

    u = []
    # subset_sums contains all possible sums of elements in u.
    # Initializing with {0} allows checking the candidate u_n itself (0 + candidate).
    subset_sums = {0}
    candidate = 1

    while len(u) < 14:
        # Since the sequence must be strictly increasing,
        # u_n must be larger than u_{n-1}.
        candidate += 1

        # A candidate is valid if for every previous subset sum 's',
        # the new subset sum (candidate + s) is not a perfect square.
        is_valid = True
        for s in subset_sums:
            if is_square(candidate + s):
                is_valid = False
                break

        if is_valid:
            # If valid, calculate all new subset sums involving this candidate.
            # New sums are {candidate + s for s in subset_sums}.
            new_sums = [candidate + s for s in subset_sums]
            for ns in new_sums:
                subset_sums.add(ns)
            u.append(candidate)

    print(f"u = {u}")
    return sum(u)

print(solve())
