def solve():
    limit = 200000
    factors = [0] * limit
    for i in range(2, limit):
        if factors[i] == 0:
            for j in range(i, limit, i):
                factors[j] += 1

    consecutive = 0
    for i in range(2, limit):
        if factors[i] == 4:
            consecutive += 1
            if consecutive == 4:
                return i - 3
        else:
            consecutive = 0

print(solve())
