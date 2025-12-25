def solve():
    # Dictionary to store cubes grouped by their sorted digits
    groups = {}
    # Since we need to ensure "exactly" four, we process cubes digit-count by digit-count
    # so we don't miss a 5th permutation later in the same digit length.
    n = 1
    while True:
        # Determine current number of digits
        d = len(str(n**3))
        groups = {}
        # Collect all cubes with exactly 'd' digits
        while True:
            cube = n**3
            s_cube = str(cube)
            if len(s_cube) > d:
                break
            key = "".join(sorted(s_cube))
            if key not in groups:
                groups[key] = []
            groups[key].append(cube)
            n += 1

        # Check if any group in this digit range has exactly 4 cubes
        candidates = []
        for key in groups:
            if len(groups[key]) == 4:
                candidates.append(min(groups[key]))

        if candidates:
            return min(candidates)

print(solve())
