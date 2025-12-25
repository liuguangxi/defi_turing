def solve():
    limit = 10000
    primes = [True] * limit
    primes[0] = primes[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            for j in range(i*i, limit, i):
                primes[j] = False

    # Store primes by their sorted digits to identify permutations
    groups = {}
    for p in range(1000, 10000):
        if primes[p]:
            key = "".join(sorted(str(p)))
            if key not in groups:
                groups[key] = []
            groups[key].append(p)

    for key in groups:
        p_list = sorted(groups[key])
        if len(p_list) < 3:
            continue

        # Check for arithmetic progression in each group
        for i in range(len(p_list)):
            for j in range(i + 1, len(p_list)):
                a = p_list[i]
                b = p_list[j]
                diff = b - a
                c = b + diff

                if c < 10000 and c in p_list:
                    if a != 1487: # Exclude the known progression
                        return a * diff

print(solve())
