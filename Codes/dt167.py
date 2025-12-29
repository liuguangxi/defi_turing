import math

n = 1
while True:
    # For a positive integer n, 2 <= n/x <= 5 is equivalent to n/5 <= x <= n/2.
    # The number of such integers x is the number of integers in [ceil(n/5), floor(n/2)].
    # Using floor division, ceil(n/5) is (n + 4) // 5 and floor(n/2) is n // 2.
    if (n // 2) - ((n + 4) // 5) + 1 == 25:
        print(n)
        break
    n += 1
