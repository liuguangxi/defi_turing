def solve():
    p, q = 3, 2
    count = 0
    for _ in range(10000):
        if len(str(p)) > len(str(q)):
            count += 1
        p, q = 2 * q + p, p + q
    return count

print(solve())
