import itertools

# Values for d^d where 0^0 = 1
powers = [i**i if i > 0 else 1 for i in range(10)]

def find_munchausen():
    # Iterate through the number of digits k (11*9^9 < 10^10, so k < 11)
    for k in range(2, 11):
        # Examine every combination of k digits (multisets)
        for combo in itertools.combinations_with_replacement(range(10), k):
            n = sum(powers[d] for d in combo)
            # Check if the sum has k digits and its digits match the combination
            if 10**(k-1) <= n < 10**k:
                if sorted(int(d) for d in str(n)) == list(combo):
                    return n

print(find_munchausen())
