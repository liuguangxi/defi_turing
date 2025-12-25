def persistence(n):
    p = 0
    while n >= 10:
        prod = 1
        for digit in str(n):
            prod *= int(digit)
        n = prod
        p += 1
    return p

def solve():
    max_p = -1
    best_n = 0
    for n in range(1, 1000000):
        # Optimization: numbers with 0 have p=1 if n > 10
        # and digits are usually sorted in best candidates.
        p = persistence(n)
        if p > max_p:
            max_p = p
            best_n = n
    return best_n

print(solve())
