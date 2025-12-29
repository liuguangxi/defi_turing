import math
from itertools import permutations

def solve():
    white_cards = [2, 3, 4, 5, 6]
    red_cards = [3, 4, 5, 6]

    def gcd(a, b):
        return math.gcd(a, b)

    count = 0
    # Pattern must be W R W R W R W R W to use all cards and alternate
    for w_p in permutations(white_cards):
        for r_p in permutations(red_cards):
            # Form the 9-digit sequence
            s = [w_p[0], r_p[0], w_p[1], r_p[1], w_p[2], r_p[2], w_p[3], r_p[3], w_p[4]]

            valid = True
            for i in range(len(s)):
                # Identify neighbors for the current card
                neighbors = []
                if i > 0:
                    neighbors.append(s[i-1])
                if i < len(s) - 1:
                    neighbors.append(s[i+1])

                # Check if the card shares a factor > 1 with at least one neighbor
                if not any(gcd(s[i], n) > 1 for n in neighbors):
                    valid = False
                    break

            if valid:
                count += 1

    return count

print(solve())
