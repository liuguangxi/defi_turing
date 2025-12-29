limit = 300000
prime = [True] * (limit + 1)
for i in range(2, int(limit**0.5) + 1):
    if prime[i]:
        for j in range(i*i, limit + 1, i):
            prime[j] = False

def solve():
    # The Perrin sequence P(n) satisfies the recurrence P(n) = P(n-2) + P(n-3).
    # Its terms are the traces of powers of the companion matrix M of x^3 - x - 1.
    # P(n) is the trace of x^n in the ring Z_n[x] / (x^3 - x - 1).
    for n in range(19, limit + 1):
        if not prime[n]:
            # Binary exponentiation for x^n mod (x^3 - x - 1, n)
            # Representation: a0 + a1*x + a2*x^2
            a0, a1, a2 = 1, 0, 0
            b0, b1, b2 = 0, 1, 0
            k = n
            while k:
                if k & 1:
                    # Multiply: (a0+a1*x+a2*x^2) * (b0+b1*x+b2*x^2)
                    c0, c1, c2, c3, c4 = a0*b0, a0*b1+a1*b0, a0*b2+a1*b1+a2*b0, a1*b2+a2*b1, a2*b2
                    # Use x^3 = x + 1 and x^4 = x^2 + x
                    a0, a1, a2 = (c0+c3)%n, (c1+c3+c4)%n, (c2+c4)%n
                # Square the base
                c0, c1, c2, c3, c4 = b0*b0, 2*b0*b1, 2*b0*b2+b1*b1, 2*b1*b2, b2*b2
                b0, b1, b2 = (c0+c3)%n, (c1+c3+c4)%n, (c2+c4)%n
                k >>= 1
            # Tr(a0 + a1*x + a2*x^2) = a0*Tr(1) + a1*Tr(x) + a2*Tr(x^2)
            # Tr(1) = 3, Tr(x) = 0, Tr(x^2) = 2
            if (3 * a0 + 2 * a2) % n == 0:
                return n

print(solve())
