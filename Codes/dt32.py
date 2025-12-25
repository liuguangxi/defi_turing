def solve():
    products = set()

    # Possible ranges for the multiplicand 'a'
    # 'a' can be 1-digit or 2-digits.
    # If 'a' is 1-digit, 'b' must be 4-digits to reach 9 total.
    # If 'a' is 2-digits, 'b' must be 3-digits to reach 9 total.
    for a in range(1, 100):
        for b in range(1, 10000):
            prod = a * b
            s = str(a) + str(b) + str(prod)

            if len(s) == 9:
                if "".join(sorted(s)) == "123456789":
                    products.add(prod)
            elif len(s) > 9:
                # If s is already too long, larger b won't help
                break

    return sum(products)

print(solve())
