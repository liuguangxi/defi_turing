coords = {
    1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (0, 3), 5: (0, 4),
    6: (1, 4), 7: (2, 4), 8: (3, 4), 9: (4, 4), 10: (4, 3),
    11: (4, 2), 12: (4, 1), 13: (4, 0), 14: (3, 0), 15: (2, 0),
    16: (1, 0), 17: (1, 1), 18: (1, 2), 19: (1, 3), 20: (2, 3),
    21: (3, 3), 22: (3, 2), 23: (3, 1), 24: (2, 1), 25: (2, 2)
}

row_digits = [[False]*4 for _ in range(5)]
col_digits = [[False]*4 for _ in range(5)]
row_count = [0]*5
col_count = [0]*5
selected = []

def backtrack(seq_idx, last_box):
    if seq_idx == 15:
        return all(c == 3 for c in row_count) and all(c == 3 for c in col_count)

    val = (seq_idx % 3) + 1
    for box_idx in range(last_box + 1, 26):
        if 15 - seq_idx > 25 - box_idx + 1: break
        r, c = coords[box_idx]
        if row_count[r] < 3 and col_count[c] < 3 and not row_digits[r][val] and not col_digits[c][val]:
            row_digits[r][val] = col_digits[c][val] = True
            row_count[r] += 1
            col_count[c] += 1
            selected.append((box_idx, val))
            if backtrack(seq_idx + 1, box_idx): return True
            selected.pop()
            row_count[r] -= 1
            col_count[c] -= 1
            row_digits[r][val] = col_digits[c][val] = False
    return False

# Starting with box 1 containing 1
r, c = coords[1]
row_digits[r][1] = col_digits[c][1] = True
row_count[r] = col_count[c] = 1
selected.append((1, 1))

if backtrack(1, 1):
    print(sum(box * val for box, val in selected))
