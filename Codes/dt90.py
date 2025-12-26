def solve():
    # Number of lamps and number of children
    num_lamps = 276
    num_children = 25

    # Initialize all lamps to False (Off)
    lamps = [False] * (num_lamps + 1)

    # Each child k toggles all multiples of k
    for k in range(1, num_children + 1):
        for lamp_idx in range(k, num_lamps + 1, k):
            lamps[lamp_idx] = not lamps[lamp_idx]

    # Count how many lamps are True (On)
    return sum(lamps)

print(solve())
