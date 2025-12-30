import collections

def solve():
    # Grid dimensions: 5 rows by 7 columns
    H, W = 5, 7
    N_SQUARES = H * W
    FULL_GRID = (1 << N_SQUARES) - 1

    # Precompute masks to handle neighbors without wrap-around
    # NOT_LEFT_COL has bits set for all columns except the first
    NOT_LEFT_COL = 0
    for r in range(H):
        for c in range(1, W):
            NOT_LEFT_COL |= (1 << (r * W + c))

    # NOT_RIGHT_COL has bits set for all columns except the last
    NOT_RIGHT_COL = 0
    for r in range(H):
        for c in range(W - 1):
            NOT_RIGHT_COL |= (1 << (r * W + c))

    # Precompute neighbor masks for each square for non-adjacency check
    neighbors_mask = []
    for i in range(N_SQUARES):
        m = 0
        r, c = divmod(i, W)
        if r > 0: m |= (1 << (i - W))
        if r < H - 1: m |= (1 << (i + W))
        if c > 0: m |= (1 << (i - 1))
        if c < W - 1: m |= (1 << (i + 1))
        neighbors_mask.append(m)

    def get_steps(start_mask):
        """Simulates the contagion and returns the number of steps to fill the grid."""
        current = start_mask
        step = 0
        while current != FULL_GRID:
            # Shift the grid to find neighbor counts bitwise
            s1 = (current << 1) & NOT_LEFT_COL
            s2 = (current >> 1) & NOT_RIGHT_COL
            s3 = (current << W)
            s4 = (current >> W)

            # c2: bits where at least 2 neighbors are infected
            c2 = (s1 & s2) | (s1 & s3) | (s1 & s4) | (s2 & s3) | (s2 & s4) | (s3 & s4)
            # c3: bits where at least 3 neighbors are infected
            c3 = (s1 & s2 & s3) | (s1 & s2 & s4) | (s1 & s3 & s4) | (s2 & s3 & s4)

            # Rule: uninfected squares with exactly 2 infected neighbors
            new_bits = (c2 & ~c3) & ~current

            if not new_bits:
                return -1 # Contamination stopped before filling

            current |= new_bits
            step += 1
        return step

    results = collections.defaultdict(int)

    def generate_non_adjacent(k, start_idx, current_mask):
        """Recursively generates all starting grids with k pairwise non-adjacent squares."""
        if k == 0:
            s = get_steps(current_mask)
            if s != -1:
                results[s] += 1
            return

        for i in range(start_idx, N_SQUARES):
            # Check if square i is adjacent to any square in the current selection
            if not (neighbors_mask[i] & current_mask):
                generate_non_adjacent(k - 1, i + 1, current_mask | (1 << i))

    # Starting with exactly 6 non-adjacent infected squares
    generate_non_adjacent(6, 0, 0)

    # Calculate sum of k * N(k)
    return sum(k * count for k, count in results.items())

print(solve())
