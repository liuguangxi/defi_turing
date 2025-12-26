def get_coords(n):
    import math
    r = math.ceil(math.sqrt(n))
    row_coord = (r-1)**2 + 1
    center = r**2 - r + 1
    k = n - center
    r_min = abs(k) + 1
    col_coord = r_min**2 - r_min + 1 + k
    return row_coord, col_coord

r, c = get_coords(2014)
print(r * c)
