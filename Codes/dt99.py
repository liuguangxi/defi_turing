def solve():
    # The sequence is defined as U_n = U_{n-1} + U_{n-2} + U_{n-3} + U_{n-4}
    # Initial terms:
    u1 = 1           # 13^0
    u2 = 13          # 13^1
    u3 = 169         # 13^2
    u4 = 2014        # Given

    # Store the latest four terms to calculate the next one
    terms = [u1, u2, u3, u4]

    # Calculate terms from index 5 up to 2014
    for _ in range(5, 2015):
        next_term = sum(terms)
        # Keep only the last four terms to save memory
        terms.pop(0)
        terms.append(next_term)

    # The 2014th term is the last element in our list
    u2014 = terms[-1]

    # Return the number of digits
    return len(str(u2014))

print(solve())
