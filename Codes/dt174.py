import math

def p_inv(n):
    # The probability that n points on a circle all lie in some semicircle
    # is given by p(n) = n / 2^(n-1).
    # We are looking for the smallest integer value of 1/p(n) = 2^(n-1) / n
    # that is greater than 10,000.
    return (2**(n - 1)) / n

n = 1
while True:
    val = int(p_inv(n))
    if math.fabs(val - p_inv(n)) < 1e-16 and val > 10000:
        print(val)
        break
    n += 1
