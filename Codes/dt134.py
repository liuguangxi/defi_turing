def solve():
    # allowed represents two-digit numbers that are not multiples of 10 or 11.
    # These are numbers of the form 10*x + y where x, y are in {1, ..., 9} and x != y.
    allowed = []
    for x in range(1, 10):
        for y in range(1, 10):
            if x != y:
                allowed.append(10 * x + y)

    # We are looking for years Y such that Y = a^2 - b^2 = c^2 - d^2,
    # with a, b, c, d in allowed and (c, d) = (rev(a), rev(b)).
    results = set()
    for i in range(len(allowed)):
        for j in range(len(allowed)):
            a = allowed[i]
            b = allowed[j]
            if a > b:
                # Calculate reversal
                ra = int(str(a)[::-1])
                rb = int(str(b)[::-1])
                y = a**2 - b**2
                # The property is Y = a^2 - b^2 = ra^2 - rb^2
                if ra > rb and ra**2 - rb**2 == y:
                    # Filter for years in the 6th millennium (5001 to 6000 inclusive).
                    if 5001 <= y <= 6000:
                        results.add(y)

    return sum(results)

print(solve())
