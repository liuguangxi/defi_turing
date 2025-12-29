def sum_cubes(n):
    return sum(int(d)**3 for d in str(n))

def reaches_153(n):
    seen = set()
    curr = n
    while curr not in seen:
        if curr == 153:
            return True
        seen.add(curr)
        curr = sum_cubes(curr)
    return False

# The 3rd millennium spans from the year 2001 to the year 3000 inclusive.
print(sum(y for y in range(2001, 3001) if reaches_153(y)))
