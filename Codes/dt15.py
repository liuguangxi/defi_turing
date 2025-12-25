import itertools

def solve():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    min_b = float('inf')
    max_b = 0

    # Iterate through all permutations of numbers 1 to 9
    for p in itertools.permutations(nums):
        # Calculate row products and column products
        b = (p[0]*p[1]*p[2] + p[3]*p[4]*p[5] + p[6]*p[7]*p[8] +
             p[0]*p[3]*p[6] + p[1]*p[4]*p[7] + p[2]*p[5]*p[8])

        if b < min_b:
            min_b = b
        if b > max_b:
            max_b = b

    return min_b, max_b, min_b * max_b

min_val, max_val, product = solve()
print(f"Min: {min_val}, Max: {max_val}, Result: {product}")
print(product)
