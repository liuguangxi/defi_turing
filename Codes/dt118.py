def solve():
    nums = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12]
    n = len(nums)
    adj = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0:
                adj[i][j] = adj[j][i] = True

    memo = {}

    def count_paths(mask, last):
        if mask == (1 << n) - 1:
            return 1
        state = (mask, last)
        if state in memo:
            return memo[state]

        count = 0
        for next_node in range(n):
            if not (mask & (1 << next_node)) and adj[last][next_node]:
                count += count_paths(mask | (1 << next_node), next_node)

        memo[state] = count
        return count

    return sum(count_paths(1 << i, i) for i in range(n))

print(solve())
