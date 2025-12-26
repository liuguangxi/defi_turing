def solve():
    n = 200
    # partitions[i] stores the number of ways to write i as a sum of positive integers
    partitions = [0] * (n + 1)
    partitions[0] = 1

    # Standard dynamic programming approach to find the number of partitions of n
    for i in range(1, n): # Only use parts up to n-1 to ensure at least two integers
        for j in range(i, n + 1):
            partitions[j] += partitions[j - i]

    return partitions[n]

print(solve())
