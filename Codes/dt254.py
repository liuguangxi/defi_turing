def solve():
    R, C = 5, 8
    # Fault lines exist between columns (vertical faults) or rows (horizontal faults).
    # A fault line is only possible if it divides the grid into two sub-grids of even area.
    # For a 5x8 grid:
    # Vertical faults at x in {2, 4, 6} (since 5 * x must be even).
    # Horizontal faults at y in {1, 2, 3, 4} (since 8 * y is always even).
    v_faults = [i for i in range(1, C) if (R * i) % 2 == 0]
    h_faults = [i for i in range(1, R) if (C * i) % 2 == 0]

    memo = {}

    def count(r, c, mask, vf_mask, hf_mask, mode):
        # Base cases: end of column, then end of grid.
        if r == R:
            return count(0, c + 1, mask, vf_mask, hf_mask, mode)
        if c == C:
            if mode == 'all':
                return 1
            # In flawless mode, all possible fault lines must have been crossed.
            return 1 if vf_mask == (1 << len(v_faults)) - 1 and hf_mask == (1 << len(h_faults)) - 1 else 0

        state = (r, c, mask, vf_mask, hf_mask, mode)
        if state in memo:
            return memo[state]

        res = 0
        if mask & (1 << r):
            # Cell is already occupied by a horizontal domino from the previous column.
            res = count(r + 1, c, mask ^ (1 << r), vf_mask, hf_mask, mode)
        else:
            # Place a horizontal domino: (r, c) and (r, c+1).
            if c + 1 < C:
                new_vf = vf_mask
                if mode == 'flawless' and (c + 1) in v_faults:
                    new_vf |= (1 << v_faults.index(c + 1))
                res += count(r + 1, c, mask | (1 << r), new_vf, hf_mask, mode)

            # Place a vertical domino: (r, c) and (r+1, c).
            if r + 1 < R and not (mask & (1 << (r + 1))):
                new_hf = hf_mask
                if mode == 'flawless' and (r + 1) in h_faults:
                    new_hf |= (1 << h_faults.index(r + 1))
                res += count(r + 2, c, mask, vf_mask, new_hf, mode)

        memo[state] = res
        return res

    A = count(0, 0, 0, 0, 0, 'all')
    print(f"A = {A}")
    memo.clear()
    B = count(0, 0, 0, 0, 0, 'flawless')
    print(f"B = {B}")
    return A * B

print(solve())
