import math

def solve_iterated_bisector_triangle():
    # Define the initial vertices of triangle ABC
    # ABC is an isosceles right triangle with the right angle at A.
    # We place A at the origin (0,0), B at (1,0), and C at (0,1).
    # This makes the side length AB = 1, so the ratio AG/AB is simply the distance AG.
    v1 = (0.0, 0.0) # Vertex A
    v2 = (1.0, 0.0) # Vertex B
    v3 = (0.0, 1.0) # Vertex C

    # Iterate the transformation: take the feet of the angle bisectors as the new vertices.
    # The process converges geometrically, so 1000 iterations provide extreme precision.
    for _ in range(1000):
        # Calculate the distances between the vertices of the current triangle.
        d12 = math.hypot(v1[0] - v2[0], v1[1] - v2[1])
        d23 = math.hypot(v2[0] - v3[0], v2[1] - v3[1])
        d31 = math.hypot(v3[0] - v1[0], v3[1] - v1[1])

        # Stop once the triangle has effectively converged to a point.
        if d12 < 1e-16:
            break

        # Compute the feet of the angle bisectors.
        # The foot of the bisector from vertex V_i divides the opposite side
        # in the ratio of the lengths of the two adjacent sides.

        # Foot from v1 on side v2-v3
        nv1 = ((d31 * v2[0] + d12 * v3[0]) / (d31 + d12),
               (d31 * v2[1] + d12 * v3[1]) / (d31 + d12))

        # Foot from v2 on side v1-v3
        nv2 = ((d23 * v1[0] + d12 * v3[0]) / (d23 + d12),
               (d23 * v1[1] + d12 * v3[1]) / (d23 + d12))

        # Foot from v3 on side v1-v2
        nv3 = ((d23 * v1[0] + d31 * v2[0]) / (d23 + d31),
               (d23 * v1[1] + d31 * v2[1]) / (d23 + d31))

        # Update vertices for the next generation ("son triangle")
        v1, v2, v3 = nv1, nv2, nv3

    # The point G is the limit of the sequence of vertices.
    g_x, g_y = v1
    # Original A was (0,0), so AG = hypot(G_x, G_y).
    # Since AB was set to 1.0, the ratio AG/AB is just ag.
    ag = math.hypot(g_x, g_y)

    # Format the result to 9 decimal places as requested.
    return f"{ag:.9f}"

result = solve_iterated_bisector_triangle()
print(f"ratio = {result}")
print(str(result)[2:])
