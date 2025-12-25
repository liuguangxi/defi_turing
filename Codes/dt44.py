def is_pentagonal(n):
    if n < 1: return False
    test = (1 + 24 * n)**0.5
    return test == int(test) and int(test) % 6 == 5

def solve():
    p = []
    n = 1
    while True:
        pk = n * (3 * n - 1) // 2
        for pj in reversed(p):
            if is_pentagonal(pk - pj) and is_pentagonal(pk + pj):
                return pk - pj
        p.append(pk)
        n += 1

print(solve())
