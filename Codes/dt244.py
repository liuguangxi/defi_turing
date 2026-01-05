cubes = [i**3 for i in range(10)]

def f(n):
    s = 0
    while n:
        s += cubes[n % 10]
        n //= 10
    return s

memo = [0] * 4375
for i in range(4375):
    path = [i]
    seen = {i}
    while True:
        nxt = f(path[-1])
        path.append(nxt)
        if nxt in seen:
            break
        seen.add(nxt)
    memo[i] = len(path)

max_l, ans = 0, 0
for n in range(1, 1000000):
    l = memo[n] if n < 4375 else memo[f(n)] + 1
    if l > max_l:
        max_l, ans = l, n

print(ans)
