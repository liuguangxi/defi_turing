def hamming(n):
    h = [1] * n
    i2 = i3 = i5 = 0
    for i in range(1, n):
        h[i] = min(h[i2] * 2, h[i3] * 3, h[i5] * 5)
        if h[i] == h[i2] * 2: i2 += 1
        if h[i] == h[i3] * 3: i3 += 1
        if h[i] == h[i5] * 5: i5 += 1
    return h

# Problem sequence starts at 2, so the 2013th term is the 2014th term of the sequence starting with 1.
res = hamming(2014)
print(f"2013th term: {res[2013]}")
print(res[2013])
