def solve():
    # Set the upper limit for the starting integer n
    upper_limit = 50000
    # Buffer to handle sequences extending beyond the upper limit
    limit = upper_limit + 100

    # Precompute the number of divisors for each integer up to the limit
    # This uses a sieve-like approach, which is efficient: O(N log N)
    divs = [0] * limit
    for i in range(1, limit):
        for j in range(i, limit, i):
            divs[j] += 1

    max_len = 0
    smallest_n = 0

    # Check each integer n < 50,000 to find the length of the run starting at n
    for n in range(1, upper_limit):
        target_divs = divs[n]
        length = 1
        # Continue extending the sequence as long as subsequent integers
        # have the same number of divisors
        while n + length < limit and divs[n + length] == target_divs:
            length += 1

        # If we find a longer sequence, update the maximum length and starting n
        if length > max_len:
            max_len = length
            smallest_n = n

    return smallest_n

# Compute the answer
result = solve()
print(result)
