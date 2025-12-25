def get_next_term(s):
    result = []
    i = 0
    n = len(s)
    while i < n:
        count = 1
        # Count consecutive identical digits
        while i + 1 < n and s[i] == s[i + 1]:
            i += 1
            count += 1
        # Append count and the digit itself
        result.append(str(count))
        result.append(s[i])
        i += 1
    return "".join(result)

def solve():
    # Sequence starts with 2
    term = "2"
    # Iterate 49 times to reach T_50
    for _ in range(49):
        term = get_next_term(term)

    # Count the number of '1's in the 50th term
    return term.count('1')

print(solve())
