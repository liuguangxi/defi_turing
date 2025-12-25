def solve():
    n = 1
    while True:
        # Optimization: n and 6n must have the same number of digits
        # This means the first digit of n must be '1'
        s_n = sorted(str(n))
        if all(sorted(str(i * n)) == s_n for i in range(2, 7)):
            return n
        n += 1

print(solve())
