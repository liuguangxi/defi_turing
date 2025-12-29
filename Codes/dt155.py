import math
from collections import Counter

def gcd_list(l):
    g = l[0]
    for x in l[1:]:
        g = math.gcd(g, x)
        if g == 1: return 1
    return g

def get_areas(W, H, e, f):
    # Formulas for the 8 areas based on intersections of DE, EC, FB, FC
    d1 = 2 * (H * W - e * f)
    d2 = 2 * (H * W + W * f - e * f)
    d3 = 2 * (W * H + e * H - e * f)

    n1 = e * f * (2 * H * W - e * H - f * W)
    if n1 % d1: return None
    s1 = n1 // d1

    n2 = f * H * (W - e)**2
    if n2 % d2: return None
    s2 = n2 // d2

    n3 = e * W * (H - f)**2
    if n3 % d3: return None
    s3 = n3 // d3

    n5 = H**2 * W * (W - e)
    if n5 % d2: return None
    s5 = n5 // d2

    n6 = W**2 * H * (H - f)
    if n6 % d3: return None
    s6 = n6 // d3

    den7 = (d1 * d2) // 2
    n7 = f**2 * H * W * (W - e)**2
    if n7 % den7: return None
    s7 = n7 // den7

    den8 = (d1 * d3) // 2
    n8 = e**2 * W * H * (H - f)**2
    if n8 % den8: return None
    s8 = n8 // den8

    s_sum = s1 + s2 + s3 + s5 + s6 + s7 + s8
    s4 = W * H - s_sum
    if s4 <= 0: return None

    return (s1, s2, s3, s4, s5, s6, s7, s8)

configs = {}
for W in range(1, 101):
    for H in range(1, W + 1):
        for e in range(1, W):
            for f in range(1, H):
                areas = get_areas(W, H, e, f)
                if areas and gcd_list(areas) == 1:
                    aset = tuple(sorted(areas))
                    # Principal configuration is the one with minimal AB
                    if aset not in configs or W < configs[aset][0]:
                        configs[aset] = (W, W * H)

N = len(configs)
total_areas = [v[1] for v in configs.values()]
counts = Counter(total_areas)
# k is the number of area values obtained twice
k_areas = [a for a, c in counts.items() if c == 2]
P = sum(k_areas)
print(f"N = {N}, P = {P}")
print(N * P)
