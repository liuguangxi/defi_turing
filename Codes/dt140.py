def get_value(x, y):
    """
    Returns the number assigned to grid coordinates (x, y)
    following the spiral path described in the problem.
    (0,0) is the bottom-left corner of the grid.
    """
    n = max(x, y) + 1
    v_start = (n - 1)**2 + 1
    if n % 2 != 0:  # Odd layer
        # Odd layers start at (0, n-1), move right to (n-1, n-1), then down to (n-1, 0)
        if y == n - 1:
            return v_start + x
        else:
            return n**2 - y
    else:  # Even layer
        # Even layers start at (n-1, 0), move up to (n-1, n-1), then left to (0, n-1)
        if x == n - 1:
            return v_start + y
        else:
            return n**2 - x

def solve():
    # Grid size is 100x100, points numbered 1 to 10,000.
    # The diagonal from top-left (0, 99) to bottom-right (99, 0)
    # consists of points with coordinates (k, 99-k) for k in 0...99.
    total_sum = sum(get_value(k, 99 - k) for k in range(100))
    print(total_sum)

solve()
