def solve():
    limit = 1000
    # Precompute U(m): number of unique products kb for k in 1..m, b in 2..limit
    u = [0] * 11
    for m in range(1, 11):
        unique_products = set()
        for k in range(1, m + 1):
            for b in range(2, limit + 1):
                unique_products.add(k * b)
        u[m] = len(unique_products)

    visited = [False] * (limit + 1)
    total_distinct = 0

    for x in range(2, limit + 1):
        if visited[x]:
            continue

        # x is a primitive base. Find how many powers of x are <= limit.
        m = 0
        curr = x
        while curr <= limit:
            visited[curr] = True
            m += 1
            curr *= x

        # Add the count of unique exponents for this primitive base
        total_distinct += u[m]

    return total_distinct

print(solve())
