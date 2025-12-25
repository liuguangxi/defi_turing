def solve():
    # Initial terms F_1 and F_2
    a, b = 1, 1
    index = 2
    target_digits = 2013

    # Iterate through the sequence
    while True:
        # Move to the next term: F_n = F_{n-1} + F_{n-2}
        a, b = b, a + b
        index += 1

        # Check digit count by converting to string or using log
        if len(str(b)) >= target_digits:
            return index

print(solve())
