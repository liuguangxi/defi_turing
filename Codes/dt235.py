import math

def is_connected(grid_size, shaded_mask):
    """
    Check if all unshaded (white) cells are connected in the grid.
    """
    white_cells = [(r, c) for r in range(grid_size) for c in range(grid_size)
                   if not (shaded_mask & (1 << (r * grid_size + c)))]
    if not white_cells:
        return False

    start = white_cells[0]
    visited = {start}
    stack = [start]
    while stack:
        r, c = stack.pop()
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < grid_size and 0 <= nc < grid_size:
                if (nr, nc) not in visited and not (shaded_mask & (1 << (nr * grid_size + nc))):
                    visited.add((nr, nc))
                    stack.append((nr, nc))
    return len(visited) == len(white_cells)

def get_primes(n):
    """
    Returns the first n prime numbers.
    """
    primes = []
    num = 2
    while len(primes) < n:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            primes.append(num)
        num += 1
    return primes

def solve_hitori(grid):
    """
    Solves the Hitori puzzle given a grid of letters.
    Returns the 0-indexed positions of the shaded squares.
    """
    size = len(grid)
    states = [0] * (size * size)  # 0: unknown, 1: shaded (black), 2: unshaded (white)

    def check_valid(idx, val):
        r, c = divmod(idx, size)
        if val == 1:  # Attempting to shade
            # Rule: No two squares adjacent on one side can both be blackened
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < size and 0 <= nc < size:
                    if states[nr * size + nc] == 1:
                        return False
        else:  # Attempting to leave white
            # Rule: Each row and column must contain unique letters among white squares
            for cc in range(size):
                if cc != c and states[r * size + cc] == 2 and grid[r][cc] == grid[r][c]:
                    return False
            for rr in range(size):
                if rr != r and states[rr * size + c] == 2 and grid[rr][c] == grid[r][c]:
                    return False
        return True

    def backtrack(idx):
        if idx == size * size:
            # Check final connectivity constraint
            mask = sum(1 << i for i, v in enumerate(states) if v == 1)
            return is_connected(size, mask)

        r, c = divmod(idx, size)
        # Optimization: Identify if a cell has duplicates in its row or column
        has_dup = any(grid[r][cc] == grid[r][c] for cc in range(size) if cc != c) or \
                  any(grid[rr][c] == grid[r][c] for rr in range(size) if rr != r)

        # If no duplicates exist, the cell must be white. Otherwise, try both possibilities.
        choices = [1, 2] if has_dup else [2]
        for val in choices:
            if check_valid(idx, val):
                states[idx] = val
                if backtrack(idx + 1):
                    return True
                states[idx] = 0
        return False

    if backtrack(0):
        return [i for i, v in enumerate(states) if v == 1]
    return []

# 8x8 grid definition from the problem
grid = [
    ['A', 'B', 'E', 'F', 'H', 'E', 'D', 'C'],
    ['F', 'B', 'A', 'G', 'G', 'H', 'C', 'A'],
    ['H', 'G', 'F', 'B', 'D', 'C', 'G', 'E'],
    ['D', 'D', 'E', 'A', 'F', 'F', 'H', 'G'],
    ['C', 'E', 'G', 'G', 'A', 'D', 'C', 'F'],
    ['H', 'A', 'G', 'D', 'C', 'E', 'F', 'D'],
    ['B', 'H', 'D', 'C', 'C', 'G', 'D', 'A'],
    ['D', 'C', 'H', 'F', 'E', 'C', 'A', 'B']
]

# Solving the puzzle and calculating the product of assigned primes
shaded_indices = solve_hitori(grid)
print(shaded_indices)
if shaded_indices:
    primes = get_primes(64)
    product = 1
    for idx in shaded_indices:
        # p_k is the k-th prime number for box k (k = idx + 1)
        product *= primes[idx]

    # Result modulo 10^13
    print(product % 10**13)
