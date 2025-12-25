import itertools

def get_neighbors(r, c):
    return [(r+dr, c+dc) for dr in [-1,0,1] for dc in [-1,0,1]
            if (dr!=0 or dc!=0) and 0<=r+dr<3 and 0<=c+dc<3]

def solve():
    cells = [(r, c) for r in range(3) for c in range(3)]
    max_fn = 0
    # Precompute neighbors
    adj = {cell: get_neighbors(*cell) for cell in cells}

    # Iterate through all starting positions for 20 and 13
    for s1, s2 in itertools.permutations(cells, 2):
        # Remaining 7 cells to be filled in some order
        rem = [c for c in cells if c != s1 and c != s2]
        for order in itertools.permutations(rem):
            grid = {} # Using dict for speed
            for c in cells: grid[c] = 0
            grid[s1] = 20
            grid[s2] = 13

            local_max = 20
            for c in order:
                s = sum(grid[nb] for nb in adj[c])
                grid[c] = s
                if s > local_max: local_max = s
            if local_max > max_fn:
                max_fn = local_max
    return max_fn

print(solve())
