def solve():
    # We are looking for six-digit numbers (100,000 to 999,999)
    # where the digit '7' appears exactly once and no digit is greater than 7.
    count = 0
    for n in range(100000, 1000000):
        s = str(n)
        # Check if 7 appears exactly once.
        if s.count('7') == 1:
            # Check if 7 is the highest digit (no digits 8 or 9).
            if '8' not in s and '9' not in s:
                count += 1
    return count

print(solve())
