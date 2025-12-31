def solve():
    """
    Problem: A sled measuring 60 units in length contains red packages with a
    minimum length of 3 units. Two packages must be separated by at least 1 unit.
    How many ways can the sled be filled?

    Let f(n) be the number of ways to fill a sled of length n.
    1. The first unit is empty: f(n-1) ways.
    2. A package of length m (3 <= m <= n) starts at the first unit:
       - If m = n, there is 1 way.
       - If m < n, there must be an empty space at unit m+1. Remaining length is n-m-1.
         There are f(n-m-1) ways.

    Recurrence: f(n) = f(n-1) + sum_{m=3}^{n-1} f(n-m-1) + 1 (for n >= 3)
    By considering f(n) - f(n-1), we derive: f(n) = 2f(n-1) - f(n-2) + f(n-4) for n >= 4.
    """
    length = 60
    # Base cases calculated using the summation recurrence:
    # f(0) = 1 (empty sled)
    # f(1) = f(0) = 1
    # f(2) = f(1) = 1
    # f(3) = f(2) + 1 = 2
    f = [1, 1, 1, 2]

    for n in range(4, length + 1):
        # f(n) = 2*f(n-1) - f(n-2) + f(n-4)
        next_val = 2 * f[n-1] - f[n-2] + f[n-4]
        f.append(next_val)

    return f[length]

print(solve())
