import itertools

def solve():
    # Distinct letters in the equation
    letters = ('T', 'H', 'R', 'E', 'N', 'I', 'O', 'S', 'U', 'F')

    # Iterate through all permutations of 0-9
    for p in itertools.permutations(range(10)):
        d = dict(zip(letters, p))

        # Rule: Leading digits cannot be zero
        if d['T'] == 0 or d['N'] == 0:
            continue

        # Define numbers based on digits
        three = d['T']*10000 + d['H']*1000 + d['R']*100 + d['E']*10 + d['E']
        nine  = d['N']*1000 + d['I']*100 + d['N']*10 + d['E']
        trois = d['T']*10000 + d['R']*1000 + d['O']*100 + d['I']*10 + d['S']
        neuf  = d['N']*1000 + d['E']*100 + d['U']*10 + d['F']

        # Constraints: Multiples of 9 and 3
        if three % 9 == 0 and neuf % 9 == 0 and nine % 3 == 0 and trois % 3 == 0:
            # Check equality
            if three * nine == trois * neuf:
                return three * nine

print(solve())
