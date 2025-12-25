def is_annular(n):
    # Green hand condition (8 fingers)
    green = (n % 14 == 2 or n % 14 == 0)
    # Blue hand condition (7 fingers)
    blue = (n % 12 == 2 or n % 12 == 0)
    return green and blue

total_sum = sum(i for i in range(1, 2014) if is_annular(i))
print(total_sum)
