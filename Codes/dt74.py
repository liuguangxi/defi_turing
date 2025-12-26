import math

def solve():
    # Precompute factorials for digits 0-9
    facts = [math.factorial(i) for i in range(10)]

    # Function to calculate the next term in the sequence
    def get_next(n):
        if n == 0:
            return 1
        s = 0
        while n:
            s += facts[n % 10]
            n //= 10
        return s

    # Memoization array for chain lengths
    # Sum of factorials for a 7-digit number < 5M is at most 7 * 9! = 2,540,160
    memo = [0] * 3000000

    # Seed known loops
    # 169 -> 363601 -> 1454 -> 169 (length 3)
    # 871 -> 45361 -> 871 (length 2)
    # 872 -> 45362 -> 872 (length 2)
    # 1 -> 1, 2 -> 2, 145 -> 145, 40585 -> 40585 (length 1)
    seeds = {
        169: 3, 363601: 3, 1454: 3,
        871: 2, 45361: 2,
        872: 2, 45362: 2,
        1: 1, 2: 1, 145: 1, 40585: 1
    }
    for k, v in seeds.items():
        if k < 3000000:
            memo[k] = v

    max_len = 0
    best_n = 0

    # Iterate through numbers less than 5 million
    for i in range(1, 5000000):
        path = []
        curr = i
        found_memo = False

        while curr not in path:
            if curr < 3000000 and memo[curr] != 0:
                length = len(path) + memo[curr]
                found_memo = True
                break
            path.append(curr)
            curr = get_next(curr)

        if not found_memo:
            # If a loop is found that wasn't in the seeds
            length = len(path)

        # Fill memo for the current path
        for j, p_val in enumerate(path):
            if p_val < 3000000:
                if memo[p_val] == 0:
                    memo[p_val] = length - j

        # Track the smallest number with the longest chain
        if length > max_len:
            max_len = length
            best_n = i

    return best_n

print(solve())
