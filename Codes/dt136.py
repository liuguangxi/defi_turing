from itertools import combinations

def solve():
    # Find five unique digits A, B, C, D, E such that A < B < C < D < E
    # and the product (10*A + B) * C = (10*D + E).
    digits = list(range(10))
    for comb in combinations(digits, 5):
        # By sorting the combination, we satisfy A < B < C < D < E.
        A, B, C, D, E = sorted(comb)

        # Define the two-digit numbers AB and DE.
        AB = A * 10 + B
        DE = D * 10 + E

        # Check the condition given in the problem.
        if AB * C == DE:
            # Format and return the concatenated string ABCDE.
            return f"{A}{B}{C}{D}{E}"

print(solve())
