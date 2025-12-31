def count_magic_hexagram():
    # Lines defined by indices 0-11
    lines = [
        (0, 1, 2, 3),
        (3, 4, 5, 6),
        (6, 7, 8, 0),
        (9, 1, 8, 10),
        (10, 2, 4, 11),
        (11, 5, 7, 9)
    ]
    target = 26
    nodes = [None] * 12
    used = [False] * 13 # 1 to 12

    count = 0

    def solve(idx):
        nonlocal count
        if idx == 12:
            # All assigned. Last checks for all lines.
            if all(sum(nodes[i] for i in line) == target for line in lines):
                count += 1
            return

        # Optimization: prune as soon as a line is complete.
        # Check L1 at idx 4 (0, 1, 2, 3)
        if idx == 4:
            if sum(nodes[i] for i in lines[0]) != target: return
        # Check L2 at idx 7 (3, 4, 5, 6)
        if idx == 7:
            if sum(nodes[i] for i in lines[1]) != target: return
        # Check L3 at idx 9 (6, 7, 8, 0)
        if idx == 9:
            if sum(nodes[i] for i in lines[2]) != target: return
        # Check L4 at idx 11 (9, 1, 8, 10)
        if idx == 11:
            # Need node 9, 1, 8, 10. Node 10 is at idx 10.
            if nodes[9] + nodes[1] + nodes[8] + nodes[10] != target: return

        for val in range(1, 13):
            if not used[val]:
                used[val] = True
                nodes[idx] = val
                solve(idx + 1)
                used[val] = False
                nodes[idx] = None

    solve(0)
    return count

print(count_magic_hexagram())
