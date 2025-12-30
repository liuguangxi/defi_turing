import math

def solve():
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    target_d = 4031
    best_n = float('inf')

    def backtrack(idx, current_n, current_d, last_e):
        nonlocal best_n
        if current_d >= target_d:
            best_n = min(best_n, current_n)
            return
        if idx == len(primes) or current_n >= best_n:
            return
        for e in range(1, last_e + 1):
            next_n = current_n * (primes[idx]**e)
            if next_n >= best_n:
                break
            backtrack(idx + 1, next_n, current_d * (2*e + 1), e)

    backtrack(0, 1, 1, 30)
    return best_n

print(solve())
