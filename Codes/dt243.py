from itertools import combinations_with_replacement

def S_p(x, p, powers):
    res = 0
    while x:
        res += powers[x % 10]
        x //= 10
    return res

def solve():
    total_G = 0
    total_H = 0
    for p in range(1, 12):
        powers = [i**p for i in range(10)]
        min_n_for_a1 = {}
        for d in combinations_with_replacement(range(10), p):
            first_idx = -1
            for i in range(p):
                if d[i] > 0:
                    first_idx = i
                    break
            if first_idx == -1:
                continue

            n = d[first_idx]
            for i in range(p):
                if i != first_idx:
                    n = n * 10 + d[i]

            a1 = 0
            for x in d:
                a1 += powers[x]
            if a1 not in min_n_for_a1 or n < min_n_for_a1[a1]:
                min_n_for_a1[a1] = n

        max_f = -1
        best_h = -1
        memo_f = {}
        for a1, n in min_n_for_a1.items():
            if a1 not in memo_f:
                curr = a1
                for _ in range(p - 1):
                    curr = S_p(curr, p, powers)
                memo_f[a1] = curr

            f = memo_f[a1]
            if f > max_f:
                max_f, best_h = f, n
            elif f == max_f:
                if n < best_h:
                    best_h = n

        total_G += max_f
        total_H += best_h

    return total_G + total_H

print(solve())
