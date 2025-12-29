for dix in range(317, 1000):
    d, i, x = str(dix)
    if len({d, i, x}) < 3: continue
    for un in range(10, 100):
        u, n = str(un)
        if u == n: continue
        res = dix**2 + un**2
        s = str(res)
        if len(s) == 6 and s[2] == n and s[5] == n and s[4] == u:
            c, e, t = s[0], s[1], s[3]
            if len({d, i, x, u, n, c, e, t}) == 8:
                print(res)
