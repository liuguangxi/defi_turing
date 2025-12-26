def is_pandigital(n):
    return set(str(n)) == set("0123456789")

# Start checking from the smallest possible 10-digit root
for x in range(31992, 100000):
    square = x * x
    if is_pandigital(square):
        print(square)
        break
