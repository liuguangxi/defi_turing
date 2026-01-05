from math import comb

def solve_h_300():
    n = 300
    # Identity
    count_g0 = 0
    for k in range(-n, n + 1):
        m = max(1, 1 - k)
        limit = (n - 3 * k) // 2
        M = limit - 3 * m
        if M >= 0:
            count_g0 += comb(M + 3, 3)

    # Rotate 60 and 300
    count_rot60 = n // 6

    # Rotate 120 and 240
    count_rot120 = 0
    M120 = n // 3
    if M120 >= 2:
        count_rot120 = comb(M120, 2)

    # Rotate 180
    count_rot180 = 0
    M180 = n // 2
    if M180 >= 3:
        count_rot180 = comb(M180, 3)

    # Reflections through vertices (3 axes)
    count_vertex_refl = 0
    for a in range(1, n // 4 + 1):
        limit = (n - 4 * a) // 2
        if limit >= 1:
            count_vertex_refl += limit

    # Reflections through edges (3 axes)
    count_edge_refl = 0
    for s1 in range(1, n):
        for s2 in range(1, n):
            limit = min(n - 2 * s1 - 3 * s2, s1 + s2 - 1)
            if limit >= 1:
                count_edge_refl += limit

    total_fixed = count_g0 + 2*count_rot60 + 2*count_rot120 + 1*count_rot180 + 3*count_vertex_refl + 3*count_edge_refl
    return total_fixed // 12

print(solve_h_300())
