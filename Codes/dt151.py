import math

area = 2016
ab = 2 * area
for a in range(1, int(math.isqrt(ab)) + 1):
    if ab % a == 0:
        b = ab // a
        c_sq = a**2 + b**2
        c = int(math.isqrt(c_sq))
        if c**2 == c_sq:
            print(f"{a}{b}{c}")
