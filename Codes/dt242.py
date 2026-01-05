def solve():
    total = 0
    # The sum ranges from n = 10 to 10^12.
    # For each k-digit integer n, F(n) is the count of k-digit integers p
    # such that mirror(p) - p = n.
    # The total sum is equivalent to counting k-digit integers p such that
    # n = mirror(p) - p has exactly k digits, for each k from 2 to 12.
    # F(10^12) for n = 10^12 (k=13) is 0 because no 13-digit integer p satisfies mirror(p) - p = 10^12.
    for k in range(2, 13):
        m = (k - 2) // 2
        # Base count b for even k, multiplied by 10 for odd k to account for the middle digit.
        b = 32 * (100**m) - 4 * (10**m)
        total += 10 * b if k % 2 else b
    return total

print(solve())
