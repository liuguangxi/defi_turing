def is_cube_divisible(n):
    d = 2
    while d * d * d <= n:
        if n % (d * d * d) == 0:
            return True
        d += 1
    return False

def solve():
    n = 1
    count = 0
    while True:
        if is_cube_divisible(n):
            count += 1
            if count == 4:
                return n - 3
        else:
            count = 0
        n += 1

print(solve())
