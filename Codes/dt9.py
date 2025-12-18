def solve_pythagorean_triplet():
    perimeter = 3600
    max_product = 0
    best_triplet = None

    # Optimization: a < b < c.
    # Since a+b+c = 3600, a must be less than 3600/3 = 1200.
    for a in range(1, perimeter // 3):
        # Using the derived formula for b
        numerator = 3600 * (1800 - a)
        denominator = 3600 - a

        if numerator % denominator == 0:
            b = numerator // denominator
            c = perimeter - a - b

            if a < b:  # Ensure unique triplet selection
                product = a * b * c
                if product > max_product:
                    max_product = product
                    best_triplet = (a, b, c)

    return max_product, best_triplet

product, triplet = solve_pythagorean_triplet()
print(f"Triplet: {triplet}")
print(product)
