def solve():
    pairs = [(x, y) for x in range(2, 100) for y in range(x + 1, 100) if x + y < 100]

    product_counts = {}
    for x, y in pairs:
        p = x * y
        product_counts[p] = product_counts.get(p, 0) + 1
    ambiguous_products = {p for p, c in product_counts.items() if c > 1}

    sum_to_pairs = {}
    for x, y in pairs:
        s = x + y
        sum_to_pairs.setdefault(s, []).append((x, y))

    simon_sure_sums = [s for s, ps in sum_to_pairs.items() if all(x*y in ambiguous_products for x, y in ps)]

    valid_after_paul = []
    for x, y in pairs:
        p, s = x * y, x + y
        if s in simon_sure_sums:
            count_simon_sure = sum(1 for x_alt in range(2, int(p**0.5) + 1) if p % x_alt == 0 and x_alt != p // x_alt and x_alt + p // x_alt < 100 and (x_alt + p // x_alt) in simon_sure_sums)
            if count_simon_sure == 1:
                valid_after_paul.append((x, y))

    for s in simon_sure_sums:
        matches = [pair for pair in sum_to_pairs[s] if pair in valid_after_paul]
        if len(matches) == 1:
            x, y = matches[0]
            print(f"X = {x}, Y = {y}, S = {x + y}, P = {x * y}")
            return x * y * (x + y) * (x * y)

print(solve())
