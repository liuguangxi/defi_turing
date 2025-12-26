def solve():
    limit = 3001
    # Precompute the number of divisors for each number up to 3001
    div_counts = [0] * (limit + 1)
    for i in range(1, limit + 1):
        for j in range(i, limit + 1, i):
            div_counts[j] += 1

    # Check the condition d(Y-1) == d(Y) == d(Y+1) for 1 < Y < 3000
    # The range(2, 3000) covers integers from 2 to 2999 inclusive.
    matching_years = []
    for y in range(2, 3000):
        if div_counts[y-1] == div_counts[y] == div_counts[y+1]:
            matching_years.append(y)

    return len(matching_years)

print(solve())
