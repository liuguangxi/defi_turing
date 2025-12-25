def is_pentagonal(n):
    # n = k(3k - 1) / 2  => 3k^2 - k - 2n = 0
    # k = (1 + sqrt(1 + 24n)) / 6
    test = (1 + 24 * n)**0.5
    return test == int(test) and int(test) % 6 == 5

def solve():
    # Every hexagonal number is also a triangular number.
    # H_m = m(2m - 1) = T_{2m-1}
    # We look for the next H_m (m > 143) that is also pentagonal.
    m = 144
    while True:
        hm = m * (2 * m - 1)
        if is_pentagonal(hm):
            return hm
        m += 1

print(solve())
