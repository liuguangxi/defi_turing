def solve():
    s_minus_i = 0
    total_sum_x = 0
    for x in range(1, 1000000):
        # Calculate x - rev(x)
        s_val = x
        i_val = int(str(x)[::-1])
        s_minus_i += (s_val - i_val)
        if s_minus_i > 0:
            total_sum_x += x
    return total_sum_x

print(solve())
