import numpy as np

def get_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            primes.append(num)
        num += 1
    return primes

def solve():
    # Grid size
    size = 8

    # Adjacency constraints (thick lines) identified from input_file_3.png
    # h_thick[r][c] is True if there is a thick line between (r, c) and (r+1, c)
    h_thick = [
        [False, False, False, False, False, False, False, True],
        [False, False, False, True, False, True, True, False],
        [True, True, False, False, True, False, True, True],
        [False, False, True, False, True, True, False, False],
        [True, True, False, True, False, True, True, True],
        [False, False, False, False, False, False, False, False],
        [False, False, False, True, True, False, False, False]
    ]

    # v_thick[c][r] is True if there is a thick line between (r, c) and (r, c+1)
    v_thick = [
        [False, False, False, True, True, False, False, False],
        [False, False, False, True, True, False, False, False],
        [True, True, False, False, True, True, True, True],
        [False, False, True, False, True, False, False, False],
        [False, False, True, True, True, True, True, False],
        [False, False, False, True, False, False, False, False],
        [False, True, False, False, False, False, False, False]
    ]

    # BFS to identify unique regions based on thick lines
    labels = [[-1] * size for _ in range(size)]
    label_count = 0
    for r in range(size):
        for c in range(size):
            if labels[r][c] == -1:
                q = [(r, c)]
                labels[r][c] = label_count
                while q:
                    cr, cc = q.pop(0)
                    if cc < 7 and not v_thick[cc][cr] and labels[cr][cc+1] == -1:
                        labels[cr][cc+1] = label_count
                        q.append((cr, cc+1))
                    if cc > 0 and not v_thick[cc-1][cr] and labels[cr][cc-1] == -1:
                        labels[cr][cc-1] = label_count
                        q.append((cr, cc-1))
                    if cr < 7 and not h_thick[cr][cc] and labels[cr+1][cc] == -1:
                        labels[cr+1][cc] = label_count
                        q.append((cr+1, cc))
                    if cr > 0 and not h_thick[cr-1][cc] and labels[cr-1][cc] == -1:
                        labels[cr-1][cc] = label_count
                        q.append((cr-1, cc))
                label_count += 1

    # Waves (Forbidden cells) from visual analysis of input_file_3.png
    forbidden = {(5, 2), (5, 3), (5, 4), (6, 3), (7, 2)}

    stars = []
    solutions = []

    def is_safe(r, c):
        if (r, c) in forbidden:
            return False
        for sr, sc in stars:
            # One star per column and no adjacent stars (including diagonals)
            if sc == c or (abs(sr - r) <= 1 and abs(sc - c) <= 1):
                return False
        # One star per region
        reg = labels[r][c]
        for sr, sc in stars:
            if labels[sr][sc] == reg:
                return False
        return True

    def backtrack(row):
        if row == size:
            solutions.append(list(stars))
            return
        for col in range(size):
            if is_safe(row, col):
                stars.append((row, col))
                backtrack(row + 1)
                stars.pop()

    backtrack(0)

    # Calculate the product of the prime numbers in the boxes containing stars
    if solutions:
        res_stars = solutions[0]
        primes = get_primes(64)
        product = 1
        for r, c in res_stars:
            k = r * 8 + c + 1  # 1-indexed box number
            product *= primes[k - 1]
        return product
    return None

print(solve())
