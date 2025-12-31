import math

def solve():
    """
    Problem:
    We draw parallel lines in different directions.
    Step 1: 2 lines in direction 1 (n1=2).
    Step 2: 3 lines in direction 2 (n2=3).
    Step 3: 4 lines in direction 3 (n3=4).
    ...
    Step k: k+1 lines in direction k (nk=k+1).

    The number of parallelograms formed by sets of parallel lines is:
    P = sum_{1 <= i < j <= k} (choose(ni, 2) * choose(nj, 2))

    Let xi = choose(i+1, 2) = (i+1)*i / 2.
    The total number of parallelograms after k steps is:
    Pk = sum_{1 <= i < j <= k} (xi * xj)

    We can calculate Pk iteratively:
    Sk = sum_{i=1}^{k} xi
    Pk = P_{k-1} + xk * S_{k-1}
    Total lines Lk = sum_{i=1}^{k} (i+1) = k*(k+3) / 2.

    We need the smallest Lk such that Pk is a multiple of 1,000,000.
    """
    P = 0
    S = 0
    # The number of parallelograms grows as O(k^6), so a solution
    # will be reached quickly.
    for k in range(1, 10000000):
        # Number of lines in the k-th direction
        nk = k + 1
        # Number of pairs of parallel lines in this direction
        xk = nk * (nk - 1) // 2

        # New parallelograms are formed by pairing the new set's
        # pairs with any pair from any previous direction set.
        P += xk * S
        S += xk

        # Check if the total count of parallelograms is a multiple of 1,000,000.
        if P > 0 and P % 1000000 == 0:
            # Total number of lines drawn up to this step.
            return k * (k + 3) // 2

# Output the minimum number of lines required.
print(solve())
