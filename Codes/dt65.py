def prod_digits(n):
    p = 1
    for d in str(n):
        p *= int(d)
    return p

def solve():
    target = 2014
    # Max P(n) for 4 digits is 9*9*9*9 = 6561? No, n <= 2014.
    # For n in [1000, 2014], max P(n) is 1*9*9*9 = 729.
    # For n in [2000, 2014], P(n) = 0.
    solutions = []
    for n in range(1, target + 1):
        if n + prod_digits(n) == target:
            if n != target:
                solutions.append(n)
    return sum(solutions)

print(solve())
