import math

def count_M_for_k_refined(n, k):
    """
    Counts permutations sigma of {1, ..., n} such that:
    1. sigma(k) = k (fixed point)
    2. sigma(1) = n
    3. The set of absolute differences {|i - sigma(i)| : i = 1, ..., n}
       is a permutation of {0, 1, ..., n-1}.
    """
    if k == 1 or k == n:
        return 0

    # Remaining positions to map: {2, 3, ..., n} \ {k}
    # Remaining values available: {1, 2, ..., n-1} \ {k}
    pos_rem = [i for i in range(2, n + 1) if i != k]
    val_rem = [i for i in range(1, n) if i != k]

    # Memoization table to optimize the backtracking
    memo = {}

    def backtrack(pos_idx, used_vals_mask, used_diffs_mask):
        state = (pos_idx, used_vals_mask, used_diffs_mask)
        if state in memo:
            return memo[state]

        if pos_idx == len(pos_rem):
            return 1

        p = pos_rem[pos_idx]
        res = 0
        for i, v in enumerate(val_rem):
            # Check if value has been used
            if not (used_vals_mask & (1 << i)):
                d = abs(p - v)
                # Differences must be distinct and non-zero (since k is the only fixed point)
                if d > 0 and d < n - 1:
                    d_bit = 1 << (d - 1)
                    if not (used_diffs_mask & d_bit):
                        res += backtrack(pos_idx + 1, used_vals_mask | (1 << i), used_diffs_mask | d_bit)

        memo[state] = res
        return res

    # sigma(k) = k and sigma(1) = n are pre-set; diffs 0 and n-1 are accounted for
    return backtrack(0, 0, 0)

def solve():
    n = 13

    # N(k) is the number of solutions where sigma(k) = k.
    # From symmetry, N(k) = M(k) + M(n + 1 - k), where M(k) counts solutions with sigma(1) = n.
    # The total sum requested is S = sum(k * N(k) for k in 1..n).
    # S = sum(k * (M(k) + M(n + 1 - k))) = (n + 1) * sum(M(k) for k in 1..n).

    m_sum = 0
    for k in range(1, n + 1):
        m_sum += count_M_for_k_refined(n, k)

    # For n = 13, the multiplier is 13 + 1 = 14.
    result = (n + 1) * m_sum
    return result

print(solve())
