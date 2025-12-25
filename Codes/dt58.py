def is_prime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def solve():
    side = 1
    prime_count = 0
    total_diagonal_elements = 1

    while True:
        side += 2
        # Corner values: side^2, side^2 - (side-1), side^2 - 2(side-1), side^2 - 3(side-1)
        # side^2 is never prime for side > 1
        corners = [side**2 - (side - 1) * i for i in range(1, 4)]

        for val in corners:
            if is_prime(val):
                prime_count += 1

        total_diagonal_elements += 4

        if prime_count / total_diagonal_elements < 0.13:
            return side

print(solve())
