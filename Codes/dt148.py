def solve():
    # We are looking for a multiplication X * Y = Total
    # X = AB1 (a three-digit number ending in 1)
    # Y = C2D (a three-digit number with 2 as the tens digit)
    # The partial products and final result have specific known digits:
    # Row 3 (P1 = X * D): . 3 . . (4 digits, the second digit is 3)
    # Row 4 (P2 = X * 2): . 4 . . (4 digits, the second digit is 4)
    # Row 5 (P3 = X * C): . 5 . . (4 digits, the second digit is 5)
    # Row 6 (Total = X * Y): 6 . . . . . (6 digits, starts with 6)

    for a in range(1, 10):
        for b in range(10):
            x = a * 100 + b * 10 + 1

            # Row 4: Partial product of X * 2
            p2 = x * 2
            # Check if p2 has 4 digits and its second digit is 4
            if not (1000 <= p2 <= 9999 and (p2 // 100) % 10 == 4):
                continue

            for d in range(10):
                # Row 3: Partial product of X * D
                p1 = x * d
                # Check if p1 has 4 digits and its second digit is 3
                if not (1000 <= p1 <= 9999 and (p1 // 100) % 10 == 3):
                    continue

                for c in range(1, 10):
                    # Row 5: Partial product of X * C
                    p3 = x * c
                    # Check if p3 has 4 digits and its second digit is 5
                    if not (1000 <= p3 <= 9999 and (p3 // 100) % 10 == 5):
                        continue

                    # Construct Y and check total product
                    y = c * 100 + 20 + d
                    total = x * y
                    # Total must be a 6-digit number starting with 6
                    if 600000 <= total <= 699999:
                        return total

# Find and print the final 6-digit number
print(solve())
