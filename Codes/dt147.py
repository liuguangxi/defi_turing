from itertools import permutations

def solve():
    # Equation: CUIRE + EN + POELE = FRIRE
    # Condition: FOC is a square (F, O, C are distinct digits).
    # Also, leading digits (C, E, P, F) cannot be zero.

    # Identify unique letters: C, U, I, R, E, N, P, O, L, F (10 distinct letters)
    letters = "CUIRENPOLF"

    # Pre-calculate 3-digit squares for FOC
    squares = []
    for i in range(10, 32):
        s = str(i * i)
        if len(set(s)) == 3:
            squares.append(s)

    for sq in squares:
        f_val, o_val, c_val = int(sq[0]), int(sq[1]), int(sq[2])
        if f_val == 0 or c_val == 0: continue

        # Digits remaining for the other 7 letters
        fixed_digits = {f_val, o_val, c_val}
        other_letters = "UIRENPL"
        rem_digits = [d for d in range(10) if d not in fixed_digits]

        for p in permutations(rem_digits, len(other_letters)):
            d = dict(zip(other_letters, p))
            d['F'], d['O'], d['C'] = f_val, o_val, c_val

            # Leading zero constraint for E and P
            if d['E'] == 0 or d['P'] == 0:
                continue

            cuire = d['C']*10000 + d['U']*1000 + d['I']*100 + d['R']*10 + d['E']
            en = d['E']*10 + d['N']
            poele = d['P']*10000 + d['O']*1000 + d['E']*100 + d['L']*10 + d['E']
            frire = d['F']*10000 + d['R']*1000 + d['I']*100 + d['R']*10 + d['E']

            if cuire + en + poele == frire:
                return frire

print(solve())
