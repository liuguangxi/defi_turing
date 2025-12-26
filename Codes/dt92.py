def solve():
    target = 2014
    # The sum of k consecutive integers starting at a is:
    # S = a + (a+1) + ... + (a+k-1) = k*a + k*(k-1)/2
    # So, target = k*a + k*(k-1)/2
    # 2 * target = 2*k*a + k^2 - k
    # 2*k*a = 2*target - k^2 + k
    # a = (2*target - k^2 + k) / (2*k)

    first_terms = []

    # Iterate through possible number of terms k
    # Since a >= 1, 2*target - k^2 + k >= 2*k => k^2 + k - 2*target <= 0
    # For target = 2014, k^2 + k - 4028 <= 0 => k is roughly <= sqrt(4028) approx 63
    for k in range(1, 65):
        numerator = 2 * target - k**2 + k
        denominator = 2 * k

        if numerator > 0 and numerator % denominator == 0:
            a = numerator // denominator
            # 'Sums' usually implies at least two terms, but the problem wording
            # 'including the example' suggests checking all mathematically valid k.
            # In similar contexts, k=1 is often excluded unless specified.
            # However, looking at the pattern of such problems, k >= 2 is standard.
            if k >= 2:
                first_terms.append(a)

    product = 1
    for val in first_terms:
        product *= val

    return product

print(solve())
