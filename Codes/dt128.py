import itertools

def solve():
    # Known values from the figure
    y_top = 1
    y_bc = 2
    y_ir = 12

    # All possible integers to fill the 10 discs (using a subset of 1 to 12)
    nums = list(range(1, 13))
    # Available integers for the remaining 7 empty discs
    others = [n for n in nums if n not in (y_top, y_bc, y_ir)]

    # We iterate through permutations of the 7 variables to be placed in the discs:
    # b1, b2, b3, b4 (the blue circles from left to right)
    # yil (yellow inner left), ybl (yellow bottom left), ybr (yellow bottom right)
    for p in itertools.permutations(others, 7):
        b1, b2, b3, b4, yil, ybl, ybr = p

        # Each of the five rows contains four numbers
        # The sum of each row and the circle of five numbers must be equal
        s1 = b1 + b2 + b3 + b4  # Horizontal blue row
        s2 = y_top + b2 + yil + ybl
        if s1 != s2: continue

        s3 = y_top + b3 + y_ir + ybr
        if s1 != s3: continue

        s4 = b1 + yil + y_bc + ybr
        if s1 != s4: continue

        s5 = b4 + y_ir + y_bc + ybl
        if s1 != s5: continue

        # Circle of five numbers (outermost circles connected by the black curve)
        sc = b1 + y_top + b4 + ybr + ybl
        if s1 != sc: continue

        # Return the concatenated number formed by the blue circles
        return f"{b1}{b2}{b3}{b4}"

print(solve())
