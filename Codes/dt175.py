def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0: return False
    return True

seq = [1]
k = 1
# We search for the 2016th tile where DP(n) = 3.
# DP(n) = 3 occurs only for the first and last tiles of each ring (Project Euler P128).
while len(seq) < 2016:
    # First tile in ring k: n = 3k^2 - 3k + 2
    # The three prime differences are 6k-1, 6k+1, and 12k+5.
    if is_prime(6*k - 1) and is_prime(6*k + 1) and is_prime(12*k + 5):
        seq.append(3*k**2 - 3*k + 2)

    # Last tile in ring k: n = 3k^2 + 3k + 1
    # The three prime differences are 6k-1, 6k+5, and 12k-7.
    # For k=1, DP(7)=2. For k=2, DP(19)=3 (one prime difference is repeated).
    if k >= 2 and is_prime(6*k - 1) and is_prime(6*k + 5) and is_prime(12*k - 7):
        seq.append(3*k**2 + 3*k + 1)

    k += 1

# Sort and retrieve the 2016th element (index 2015).
seq.sort()
print(seq[2015])
