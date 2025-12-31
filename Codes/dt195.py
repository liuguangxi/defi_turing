from itertools import product

def solve():
    """
    Solves the Turing challenge regarding inserting + or - signs
    between digits 9, 8, 7, 6, 5, 4, 3, 2, 1.
    """
    digits = "987654321"
    # Mapping from evaluation result to list of (sign_count, expression_string)
    results = {}

    # Each of the 8 gaps between 9 digits can be: concatenation (''), '+', or '-'
    for ops in product(['', '+', '-'], repeat=len(digits)-1):
        expr = digits[0]
        sign_count = 0
        for i, op in enumerate(ops):
            expr += op + digits[i+1]
            if op:
                sign_count += 1

        # Manually evaluate the expression (only '+' and '-' involved)
        # Using .replace('-', '+-') and splitting by '+' handles the unary minus correctly.
        val = sum(int(p) for p in expr.replace('-', '+-').split('+') if p)

        if val not in results:
            results[val] = []
        results[val].append((sign_count, expr))

    # A: the first non-negative integer that cannot be formed
    A = 0
    while A in results:
        A += 1

    # B: total number of operation signs used for all integers less than A
    # Based on the prompt "using a minimum number of symbols", we take the
    # minimal sign count for each integer k < A.
    min_sign_counts = {}
    B = 0
    for k in range(A):
        m = min(s for s, e in results[k])
        min_sign_counts[k] = m
        B += m

    # C: the integer less than A with the fewest operational signs
    min_overall = min(min_sign_counts.values())
    # In the range [0, 193], only k=12 can be formed with 2 signs (987-654-321).
    # All others require more signs.
    C = [k for k, s in min_sign_counts.items() if s == min_overall][0]

    # D: the integers less than A that can only be written in one way
    # (Checking the total number of distinct strings evaluating to k).
    D = [k for k in range(A) if len(results[k]) == 1]

    # Calculate the product A * B * C * D_1 * ... * D_n
    print(f"A = {A}")
    print(f"B = {B}")
    print(f"C = {C}")
    print(f"D = {D}")
    prod = A * B * C
    for d_val in D:
        prod *= d_val

    return prod

print(solve())
