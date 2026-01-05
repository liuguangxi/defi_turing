def solve():
    """
    The row of lamps follows a cellular automaton behavior similar to Rule 60.
    Let L(i, t) be the state (1 for lit, 0 for unlit) of the i-th lamp at time t.

    Conditions given:
    1. Initially (t=0), only the far-left lamp is lit: L(0, 0) = 1, L(i, 0) = 0 for i > 0.
    2. Operation: Each lamp i changes state if its left neighbor (i-1) was lit a second earlier.
       L(i, t) = L(i, t-1) XOR L(i-1, t-1) for i > 0.
    3. Leftmost lamp is always on: L(0, t) = 1.

    This recurrence relation generates Pascal's triangle modulo 2:
    L(i, t) = (t choose i) mod 2.

    The row contains 8000 lamps, so the index of the far-right lamp is 7999.
    The lamp on the far right (index 7999) turns on when L(7999, t) = 1.
    The property (t choose i) = 0 for t < i implies the rightmost lamp turns on
    for the first time at t = 7999, where L(7999, 7999) = (7999 choose 7999) mod 2 = 1.

    At t = 7999, the number of lit lamps is the count of i in {0, 1, ..., 7999}
    such that (7999 choose i) is odd.
    According to Gould's Theorem, the number of odd entries in the n-th row
    of Pascal's triangle is 2^popcount(n), where popcount(n) is the number
    of set bits in the binary representation of n.
    """
    n = 7999
    # popcount(7999) = popcount(0b1111100111111) = 11
    popcount_n = bin(n).count('1')
    return 2 ** popcount_n

print(solve())
