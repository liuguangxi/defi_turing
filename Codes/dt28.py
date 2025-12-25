def solve():
    n = 2013
    total_sum = 1  # Starting with the center '1'

    # Iterate through each odd square size from 3 to n
    for k in range(3, n + 1, 2):
        # Sum of the four corners: 4k^2 - 6k + 6
        layer_sum = 4 * k**2 - 6 * k + 6
        total_sum += layer_sum

    return total_sum

print(solve())
