def solve():
    # Search from the largest possible 7-digit numbers downwards
    for n in range(9999999, 0, -1):
        # Quick mathematical filters:
        # n must end in 8 (so 4*n ends in 2, the starting digit)
        # and n must start with 2 (so 4*n has the same number of digits)
        s_n = str(n)
        if s_n[0] == '2' and s_n[-1] == '8':
            if int(s_n[::-1]) == 4 * n:
                return n

print(solve())
