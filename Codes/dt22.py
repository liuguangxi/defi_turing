def solve():
    candidates = []
    # Search for six-digit numbers n where 8n is an anagram of n
    for n in range(100000, 125000):
        s_n = sorted(str(n))
        s_8n = sorted(str(8 * n))
        if s_n == s_8n:
            candidates.append(n)

    # The problem implies there are exactly two such numbers that are anagrams of each other
    # Based on our logic, we check the candidates found.
    return sum(candidates)

print(solve())
