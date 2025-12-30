def count_reversible_per_length(L):
    """
    Calculates the count of reversible numbers n of digit length L.
    A reversible number n satisfies:
    1. n does not end in 0.
    2. Every digit of (n + mirror(n)) is odd.
    """
    if L == 1:
        return 0

    # Case for even digit length L = 2k
    # Pattern: 20 * 30^(k-1)
    if L % 2 == 0:
        k = L // 2
        return 20 * (30 ** (k - 1))

    # Case for odd digit length L
    # If L = 1 mod 4 (e.g., 1, 5, 9), count is 0.
    if L % 4 == 1:
        return 0

    # If L = 3 mod 4 (e.g., 3, 7, 11), count follows a specific carry-chain pattern.
    # Pattern: L=3 -> 100, L=7 -> 50000. General: 20 * (500^((L-3)/4)) * 5
    # or more simply: 100 * (500 ** ((L-3)//4))
    if L % 4 == 3:
        k = (L - 3) // 4
        return 100 * (500 ** k)

    return 0

# Threshold: less than ten billion (10^10), so n can have 1 to 10 digits.
total_reversible = sum(count_reversible_per_length(L) for L in range(1, 11))
print(total_reversible)
