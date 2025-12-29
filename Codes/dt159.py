P = {2, 3, 5, 7}

def check(n):
    return all(int(d) in P for d in str(n))

def solve():
    prime_digits = [2, 3, 5, 7]
    three_digit_nums = [100*a + 10*b + c for a in prime_digits for b in prime_digits for c in prime_digits]

    for abc in three_digit_nums:
        for e in prime_digits:
            p1 = abc * e
            if 1000 <= p1 <= 9999 and check(p1):
                for d in prime_digits:
                    p2 = abc * d
                    if 1000 <= p2 <= 9999 and check(p2):
                        result = abc * (10 * d + e)
                        if 10000 <= result <= 99999 and check(result):
                            return result

print(solve())
