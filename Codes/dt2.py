def solve_odd_fibonacci(limit):
    a, b = 1, 1
    odd_sum = 0

    while a <= limit:
        if a % 2 != 0:
            odd_sum += a

        # Calculate next term: a becomes previous b,
        # b becomes the sum of the two previous
        a, b = b, a + b

    return odd_sum

limit = 4000000
result = solve_odd_fibonacci(limit)
print(result)
