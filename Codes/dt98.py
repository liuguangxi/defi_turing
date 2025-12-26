import math

def solve():
    L = 60
    # Triangles with right angle at O (0,0)
    # P is on x-axis (x1, 0), Q is on y-axis (0, y2)
    # There are L choices for x1 (1 to L) and L choices for y2 (1 to L).
    count = L * L

    # Triangles with right angle at P(x1, y1)
    # Case 1: P is on an axis.
    # If P = (x1, 0), then Q must be (x1, y2) with y2 in [1, L].
    # There are L choices for x1 and L choices for y2. (L*L triangles)
    # If P = (0, y1), then Q must be (x2, y1) with x2 in [1, L].
    # There are L choices for y1 and L choices for x2. (L*L triangles)
    count += 2 * L * L

    # Case 2: P is off the axes (x1 > 0, y1 > 0)
    # For a right angle at P, vector PQ must be perpendicular to vector OP.
    # Let OP = (x1, y1). The perpendicular direction is (-y1, x1).
    # The smallest integer step vector in this direction is v = (-y1/g, x1/g)
    # where g = gcd(x1, y1).
    for x1 in range(1, L + 1):
        for y1 in range(1, L + 1):
            g = math.gcd(x1, y1)
            dx, dy = y1 // g, x1 // g

            # Count steps k in the direction (-dx, dy)
            # Q = (x1 - k*dx, y1 + k*dy)
            # 0 <= x1 - k*dx <= L  =>  k*dx <= x1  =>  k <= x1 // dx
            # 0 <= y1 + k*dy <= L  =>  k*dy <= L - y1  =>  k <= (L - y1) // dy
            k_pos = min(x1 // dx, (L - y1) // dy)

            # Count steps k in the opposite direction (dx, -dy)
            # Q = (x1 + k*dx, y1 - k*dy)
            # 0 <= x1 + k*dx <= L  =>  k*dx <= L - x1  =>  k <= (L - x1) // dx
            # 0 <= y1 - k*dy <= L  =>  k*dy <= y1  =>  k <= y1 // dy
            k_neg = min((L - x1) // dx, y1 // dy)

            count += k_pos + k_neg

    return count

print(solve())
