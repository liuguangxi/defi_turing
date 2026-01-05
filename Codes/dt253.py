import sys

# Increase recursion depth for deep DSU trees
sys.setrecursionlimit(10000)

def solve():
    # --- Part 1: Chain of Paper Clips ---
    # With k=10 manipulations, we obtain 10 single clips and 11 sub-chains.
    # To cover every sum from 1 to L, we use a greedy approach (powers of 2).
    # 10 clips of size 1 give a range of [1, 10].
    # The next piece should be 11, then 22, 44, ..., up to the 11th sub-chain.
    # Size of the i-th sub-chain: 11 * 2**(i-1).
    # Total length L = 10 + sum(11 * 2**i for i in range(11))
    # L = 10 + 11 * (2**11 - 1) = 10 + 11 * 2047 = 22527.
    L = 10 + 11 * (2**11 - 1)
    print(f"L = {L}")

    # --- Part 2: Color Patterns ---
    n = 10000
    parent = list(range(n))

    def find(i):
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        root_i, root_j = find(i), find(j)
        if root_i != root_j:
            parent[root_i] = root_j

    # Constraint 1: Removed clips (4th, 8th, ...) match the first 2500.
    for j in range(2500):
        # 4th clip is at index 3, 8th at 7, etc.
        union(j, 4 * j + 3)

    # Constraint 2: Remaining clips match the first 7500.
    remaining_indices = [k for k in range(n) if (k + 1) % 4 != 0]
    for j in range(7500):
        union(j, remaining_indices[j])

    # Calculate sizes of the orbits (equivalence classes)
    orbit_sizes = {}
    for i in range(n):
        root = find(i)
        orbit_sizes[root] = orbit_sizes.get(root, 0) + 1

    # The colors Red, Blue, Green correspond to the classes of the first three clips.
    r0, r1, r2 = find(0), find(1), find(2)
    red_count = orbit_sizes[r0]
    blue_count = orbit_sizes[r1]
    green_count = orbit_sizes[r2]
    print(f"#R = {red_count}, #B = {blue_count}, #G = {green_count}")

    # Final Answer = Result 1 + (Product of 3 counts from Result 2)
    final_result = L + (red_count * blue_count * green_count)
    return final_result

print(solve())
