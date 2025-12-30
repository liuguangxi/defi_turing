def T(n):
    m = n // 2
    if n % 2 == 0:
        return m * (m + 1) * (4 * m - 1) // 2
    else:
        return m * (m + 1) * (4 * m + 5) // 2

for n in range(2, 1000000):
    if T(n) % 1_000_000 == 0:
        print(n)
        break
