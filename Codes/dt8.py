def find_rectangle_6400():
    target_s = 6400
    constant = target_s * 6
    best_diff = float('inf')
    best_rectangle = None

    # We iterate through possible widths.
    # Since S is approx W^3 / 3, W won't exceed ~30.
    for w in range(1, 100):
        denom = w * (w + 1)
        if constant % denom == 0:
            k = constant // denom
            # From the formula: k = 3L - W + 1
            if (k + w - 1) % 3 == 0:
                l = (k + w - 1) // 3
                if l >= w:
                    diff = l - w
                    if diff < best_diff:
                        best_diff = diff
                        best_rectangle = (l, w)

    return best_rectangle

l, w = find_rectangle_6400()
print(f"Rectangle: {l}x{w}")
print(l * w)
