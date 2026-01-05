import itertools

def solve():
    # d[i] corresponds to the blank in line (i+1).
    # target_digit[i] is the number we are counting for line (i+1).
    # target_digit = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    targets = [9, 8, 7, 6, 5, 4, 3, 2, 1]

    # We look for a tuple d = (d1, d2, ..., d9) where di in [0, 9].
    # For i != 5 (index 4), fixed count is 1. For i == 5, fixed count is 0.
    # d[i] = fixed_count + count of target_digit[i] in {d[j] for j != i}.

    for d in itertools.product(range(10), repeat=9):
        valid = True
        for i in range(9):
            target = targets[i]
            # Count target in d excluding d[i]
            current_count = sum(1 for j in range(9) if j != i and d[j] == target)

            # The digit 'target' appears in line 'target' (as label) and line '10-target' (as target).
            # Here line index is i+1. So target is 10-(i+1).
            # Digit k appears as target in line 10-k and as label in line k.
            # We are outside line i+1.
            # Digit target = 10-(i+1) appears in line 10-(target) and line target.
            # One of these is line i+1. The other is 'target'.
            # If i+1 != target, fixed count is 1. If i+1 == target, fixed count is 0.
            # (i+1 == target) is (i+1 == 10-(i+1)) => 2(i+1)=10 => i+1=5.
            fixed = 0 if (i + 1 == 5) else 1

            if d[i] != fixed + current_count:
                valid = False
                break
        if valid:
            return "".join(map(str, d))

print(solve())
