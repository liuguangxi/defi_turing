def solve():
    """
    Solves the sequence problem:
    u_1 = 1, u_2 = 2.
    u_n is either 2 * u_{n-1} or u_{n-1} + u_{n-2}.
    We need to find the largest odd u_50.

    We use dynamic programming with pruning. For each parity state of the
    last two numbers (u_i % 2, u_{i-1} % 2), we track non-dominated pairs (u_i, u_{i-1}).
    A pair (u, v) is non-dominated if no other pair (u', v') exists such that
    u' >= u and v' >= v.
    """
    # Jean writes 1 and 2.
    # Initial state: u_2 = 2, u_1 = 1. Parity: (even, odd).
    # Dictionary maps (current_parity, previous_parity) to a list of (u_current, u_prev).
    states = {(0, 1): [(2, 1)]}

    # We have 2 numbers and need to reach 50 numbers total (48 more steps).
    for _ in range(48):
        next_raw = {}
        for (p1, p2), pairs in states.items():
            for u, v in pairs:
                # Two possible choices for the next number in the sequence:
                # 1. Double the previous number: 2 * u
                # 2. Sum of the two previous numbers: u + v
                for nu, nv in [(2 * u, u), (u + v, u)]:
                    parity_state = (nu % 2, nv % 2)
                    next_raw.setdefault(parity_state, []).append((nu, nv))

        # Pruning dominated pairs to keep the state space manageable.
        # For each parity state, we sort by 'u' descending and only keep
        # pairs where 'v' is larger than any 'v' seen so far for larger 'u's.
        states = {}
        for par, pairs in next_raw.items():
            pairs.sort(key=lambda x: (x[0], x[1]), reverse=True)
            pruned_list = []
            max_v = -1
            for u, v in pairs:
                if v > max_v:
                    pruned_list.append((u, v))
                    max_v = v
            states[par] = pruned_list

    # The problem specifies that the 50th number must be odd (p1 == 1).
    odd_u50_values = [u for (p1, p2), pairs in states.items() if p1 == 1 for u, v in pairs]
    return max(odd_u50_values)

print(solve())
