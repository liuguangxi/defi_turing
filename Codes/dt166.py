counts = [0] * 55
for i in range(1000001):
    n = sum(int(d) for d in str(i))
    counts[n] += 1

print(max(counts))
