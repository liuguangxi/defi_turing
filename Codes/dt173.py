import itertools

def get_angle_steps(a, b, c):
    """Calculates the inscribed angle steps between three points on a circle."""
    l_ac = (c - a) % 8
    l_ab = (b - a) % 8
    # If b is on the clockwise arc from a to c, return the counter-clockwise arc length.
    return (a - c) % 8 if l_ab < l_ac else (c - a) % 8

pts = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
val_map = {0: ['A', 'C', 'F'], 1: ['G'], 2: ['B', 'E'], 6: ['D', 'H']}
target = [0, 2, 0, 6, 2, 0, 1, 6]

min_m, best_paths = float('inf'), []

# Iterate through all possible letter sequences for the given date numbers
for p in itertools.product(*(val_map[v] for v in target)):
    # A segment is an undirected edge between two vertices
    segs = [frozenset([p[i], p[i+1]]) for i in range(7)]
    # All 7 segments must be distinct
    if len(set(segs)) < 7:
        continue

    # Calculate sum of angle steps (each step is 22.5 degrees)
    m = sum(get_angle_steps(pts[p[i-1]], pts[p[i]], pts[p[i+1]]) for i in range(1, 7))

    if m < min_m:
        min_m, best_paths = m, [p]
    elif m == min_m:
        best_paths.append(p)

M = min_m * 22.5
P = sum(int("".join(str(ord(c) - 64) for c in path)) for path in best_paths)

print(f"M = {M}, P = {P}")
print(int(M * P))
