import math

def is_in_cross(x, y, n):
    """
    Checks if the point (x, y) is within the cross of side length n.
    The cross is defined as the union of two rectangles:
    - Horizontal: [-n, 2n-1] x [0, n-1]
    - Vertical: [0, n-1] x [-n, 2n-1]
    """
    in_horiz = (-n <= x < 2 * n) and (0 <= y < n)
    in_vert = (0 <= x < n) and (-n <= y < 2 * n)
    return in_horiz or in_vert

def count_squares(n):
    """
    Counts all squares whose four vertices are points on the cross of side length n.
    A square is uniquely identified by one vertex (x, y) and an edge vector (dx, dy)
    such that dx >= 1 and dy >= 0. This ensures each square is counted exactly once.
    """
    count = 0
    # The bounding box of the cross is [-n, 2n-1] x [-n, 2n-1].
    # The maximum possible coordinate difference is 3n - 1.
    for dx in range(1, 3 * n):
        for dy in range(0, 3 * n):
            # Optimization: only search for (x, y) such that all four vertices of
            # the square of type (dx, dy) stay within the cross's bounding box.
            # Vertices: P1(x,y), P2(x+dx,y+dy), P3(x+dx-dy,y+dy+dx), P4(x-dy,y+dx).
            x_min = dy - n
            x_max = 2 * n - dx
            y_min = -n
            y_max = 2 * n - dx - dy

            for x in range(x_min, x_max):
                for y in range(y_min, y_max):
                    # Check if all four vertices belong to the point set of the cross.
                    if (is_in_cross(x, y, n) and
                        is_in_cross(x + dx, y + dy, n) and
                        is_in_cross(x + dx - dy, y + dy + dx, n) and
                        is_in_cross(x - dy, y + dx, n)):
                        count += 1
    return count

def solve():
    """
    Calculates the sum of C(n) for n ranging from 1 to 20.
    """
    total_sum = 0
    for n in range(1, 21):
        total_sum += count_squares(n)
    return total_sum

print(solve())
