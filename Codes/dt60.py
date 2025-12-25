def josephus(n, k):
    survivor = 0  # J(1, k) = 0 (0-based)
    for i in range(2, n + 1):
        survivor = (survivor + k) % i
    return survivor + 1  # Convert to 1-based indexing

def solve():
    return josephus(2013, 7)

print(solve())
