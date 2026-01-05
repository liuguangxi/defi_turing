def get_neighbors(r, c):
    """Returns the coordinates of the 8 neighbors for a cell in a 5x5 grid."""
    return [(r + dr, c + dc) for dr in [-1, 0, 1] for dc in [-1, 0, 1]
            if (dr != 0 or dc != 0) and 0 <= r + dr < 5 and 0 <= c + dc < 5]

def get_candidates(k, grid, pos):
    """
    Finds empty cells where the value k can be placed.
    A number k > 2 must be the sum of two existing neighbors a and b (a+b=k).
    Since a, b >= 1, it follows that a < k and b < k.
    """
    candidates = set()
    for a in range(1, (k + 1) // 2):
        b = k - a
        if a == b or not pos[a] or not pos[b]:
            continue

        # Candidate cells for k must be neighbors to both pos(a) and pos(b).
        neigh_a = set(get_neighbors(*pos[a]))
        neigh_b = set(get_neighbors(*pos[b]))
        common_neighbors = neigh_a.intersection(neigh_b)

        for r, c in common_neighbors:
            if grid[r][c] == 0:
                candidates.add((r, c))
    return candidates

def backtrack(k, grid, pos):
    """Backtracking algorithm to fill the grid sequentially from 3 to 25."""
    if k == 26:
        return True

    candidates = get_candidates(k, grid, pos)

    # Check fixed constraints for values 7 (at A2) and 18 (at C3/Center).
    if k == 7:
        if (0, 1) in candidates:
            grid[0][1], pos[7] = 7, (0, 1)
            if backtrack(k + 1, grid, pos): return True
            grid[0][1], pos[7] = 0, None
        return False

    if k == 18:
        if (2, 2) in candidates:
            grid[2][2], pos[18] = 18, (2, 2)
            if backtrack(k + 1, grid, pos): return True
            grid[2][2], pos[18] = 0, None
        return False

    # For other values, try all valid candidate cells.
    for r, c in candidates:
        # Avoid cells reserved for fixed constraints.
        if (r, c) == (0, 1) or (r, c) == (2, 2):
            continue

        grid[r][c], pos[k] = k, (r, c)
        if backtrack(k + 1, grid, pos):
            return True
        grid[r][c], pos[k] = 0, None

    return False

def solve():
    """Tries all initial positions for the 'seed' values 1 and 2."""
    for r1 in range(25):
        p1 = (r1 // 5, r1 % 5)
        if p1 == (0, 1) or p1 == (2, 2): continue
        for r2 in range(25):
            p2 = (r2 // 5, r2 % 5)
            if r1 == r2 or p2 == (0, 1) or p2 == (2, 2): continue

            # Since 3 = 1 + 2, positions for 1 and 2 must share a common neighbor.
            if max(abs(p1[0] - p2[0]), abs(p1[1] - p2[1])) > 2: continue

            grid, pos = [[0] * 5 for _ in range(5)], [None] * 26
            grid[p1[0]][p1[1]], grid[p2[0]][p2[1]] = 1, 2
            pos[1], pos[2] = p1, p2

            if backtrack(3, grid, pos):
                # Calculate the sum of products: (number in cell) * (cell index 1-25).
                for row in grid:
                    print(row)
                return sum(grid[r][c] * (r * 5 + c + 1) for r in range(5) for c in range(5))

print(solve())
