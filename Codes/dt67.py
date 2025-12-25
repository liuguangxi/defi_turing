def solve(n=10000001):
    memo = {0: 0, 1: 1}

    def s(k):
        if k in memo:
            return memo[k]
        if k % 2 == 0:
            res = s(k // 2)
        else:
            m = k // 2
            res = s(m) + s(m + 1)
        memo[k] = res
        return res

    import sys
    sys.setrecursionlimit(2000)
    return s(n)

print(solve())
