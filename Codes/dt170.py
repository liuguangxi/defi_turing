from itertools import permutations

def solve():
    # Sum of integers 1 to 12 is 78.
    # The grid consists of 5 squares (unit cycles).
    # S1 (Top): x1+x2+x4+x5, S2 (Left): x3+x4+x7+x8, S3 (Center): x4+x5+x8+x9,
    # S4 (Right): x5+x6+x9+x10, S5 (Bottom): x8+x9+x11+x12.
    # Sum of S_i = 5S = Sum(x_i) + 2(x4+x5+x8+x9) = 78 + 2S => 3S = 78 => S = 26.

    nums = list(range(1, 13))
    total_count = 0

    # Iterate through all permutations of 4 numbers for the central square
    for p_center in permutations(nums, 4):
        x4, x5, x8, x9 = p_center
        if x4 + x5 + x8 + x9 != 26:
            continue

        remaining = set(nums) - set(p_center)
        R = sorted(list(remaining))

        # Targets for the remaining 4 pairs (one pair per outer square)
        targets = [26 - (x4 + x5), 26 - (x4 + x8), 26 - (x5 + x9), 26 - (x8 + x9)]

        # Precompute possible pairs from remaining numbers for each target sum
        pairs_for_t = []
        for t in targets:
            tp = [(R[i], R[j]) for i in range(8) for j in range(i + 1, 8) if R[i] + R[j] == t]
            pairs_for_t.append(tp)

        if any(not tp for tp in pairs_for_t):
            continue

        def count_assignments(idx, used_mask):
            if idx == 4:
                return 1
            ways = 0
            for a, b in pairs_for_t[idx]:
                mask_val = (1 << R.index(a)) | (1 << R.index(b))
                if not (used_mask & mask_val):
                    # Each pair (a, b) can be placed in 2 orders in its square vertices
                    ways += 2 * count_assignments(idx + 1, used_mask | mask_val)
            return ways

        total_count += count_assignments(0, 0)

    return total_count

print(solve())
