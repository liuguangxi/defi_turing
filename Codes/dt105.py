from itertools import combinations
from fractions import Fraction

def get_max_n(digits):
    memo = {}

    def get_all(subset):
        if subset in memo:
            return memo[subset]
        if len(subset) == 1:
            return {Fraction(subset[0])}

        res = set()
        size = len(subset)
        # Split the current subset into two non-empty partitions L and R.
        # Iterating up to 2**(size-1) avoids processing the same partition (L,R) and (R,L) twice.
        for i in range(1, 1 << (size - 1)):
            l_part = tuple(subset[j] for j in range(size) if (i >> j) & 1)
            r_part = tuple(subset[j] for j in range(size) if not (i >> j) & 1)

            l_vals = get_all(l_part)
            r_vals = get_all(r_part)

            for l in l_vals:
                for r in r_vals:
                    # Apply all 4 operations. Subtraction and division are handled in both directions.
                    res.update({l + r, l - r, r - l, l * r})
                    if r != 0:
                        res.add(l / r)
                    if l != 0:
                        res.add(r / l)

        memo[subset] = res
        return res

    # Calculate all possible values for the combination.
    vals = get_all(tuple(sorted(digits)))
    # Extract distinct positive integers.
    ints = {v.numerator for v in vals if v.denominator == 1 and v.numerator > 0}

    # Find the length of the string of consecutive integers 1, 2, ..., n.
    n = 0
    while n + 1 in ints:
        n += 1
    return n

def solve():
    best_n = 0
    best_combo = ""

    # Iterate through all combinations of 4 distinct digits from {0, ..., 9}.
    for combo in combinations(range(10), 4):
        curr_n = get_max_n(combo)
        if curr_n > best_n:
            best_n = curr_n
            best_combo = "".join(map(str, combo))

    print(best_combo)

solve()
