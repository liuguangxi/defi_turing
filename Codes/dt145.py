def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def solve():
    # Symmetric (reversible) 3-digit primes without any digit '0'
    primes_set = set()
    for n in range(100, 1000):
        s = str(n)
        if '0' in s: continue
        if is_prime(n) and is_prime(int(s[::-1])):
            primes_set.add(s)

    primes_list = sorted(list(primes_set))
    count = 0
    # Iterating through possible rows ABC, DEF, GHI
    for r1 in primes_list:
        for r2 in primes_list:
            if r1 == r2: continue
            for r3 in primes_list:
                if r3 == r1 or r3 == r2: continue

                # Check column strings: ADG, BEH, CFI
                c1 = r1[0] + r2[0] + r3[0]
                c2 = r1[1] + r2[1] + r3[1]
                c3 = r1[2] + r2[2] + r3[2]

                # Each column and its reversal must be prime and columns must be distinct
                if c1 not in primes_set or c2 not in primes_set or c3 not in primes_set: continue
                if c1 == c2 or c1 == c3 or c2 == c3: continue

                # Check diagonal strings: AEI, CEG
                d1 = r1[0] + r2[1] + r3[2]
                d2 = r1[2] + r2[1] + r3[0]

                # Each diagonal and its reversal must be prime
                if d1 in primes_set and d2 in primes_set:
                    count += 1
    return count

print(solve())
