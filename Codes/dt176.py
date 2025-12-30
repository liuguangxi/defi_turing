import itertools
from math import factorial

def solve():
    # Points awarded for each rank in a 4-boat race
    # 1st: 4, 2nd: 3, 3rd: 2, 4th: 1
    # Possible scores for boats {A, B, C} given D's rank k (1st to 4th)
    scores_at_k = {
        1: [3, 2, 1], # D is 1st (4 pts), others take 3, 2, 1
        2: [4, 2, 1], # D is 2nd (3 pts), others take 4, 2, 1
        3: [4, 3, 1], # D is 3rd (2 pts), others take 4, 3, 1
        4: [4, 3, 2], # D is 4th (1 pt), others take 4, 3, 2
    }

    # Relative rankings of A, B, and C in the 3 remaining slots
    abc_perms = list(itertools.permutations([0, 1, 2]))

    # Precalculate score differences and head-to-head outcomes for each (D_rank, ABC_ranking)
    # Mapping: (rank_of_D, abc_perm_index) -> (diffAB, diffBC, A_beats_B, B_beats_C, C_beats_A)
    match_data = {}
    for k in [1, 2, 3, 4]:
        available_scores = scores_at_k[k]
        for idx, p in enumerate(abc_perms):
            sa, sb, sc = available_scores[p[0]], available_scores[p[1]], available_scores[p[2]]
            match_data[(k, idx)] = (
                sa - sb,
                sb - sc,
                1 if sa > sb else 0,
                1 if sb > sc else 0,
                1 if sc > sa else 0
            )

    def count_regattas_for_d_dist(d_dist):
        """Counts valid regattas for a fixed distribution of D's ranks."""
        flat_ks = []
        for rank, count in zip([1, 2, 3, 4], d_dist):
            flat_ks.extend([rank] * count)

        # DP state: (score_diff_AB, score_diff_BC, win_count_AB, win_count_BC, win_count_CA)
        dp = {(0, 0, 0, 0, 0): 1}
        for k in flat_ks:
            new_dp = {}
            for state, count in dp.items():
                dab, dbc, wab, wbc, wca = state
                for p_idx in range(6):
                    ddab, ddbc, dwab, dwbc, dwca = match_data[(k, p_idx)]
                    new_state = (dab + ddab, dbc + ddbc, wab + dwab, wbc + dwbc, wca + dwca)
                    new_dp[new_state] = new_dp.get(new_state, 0) + count
            dp = new_dp

        valid_regattas = 0
        for (dab, dbc, wab, wbc, wca), count in dp.items():
            # Constraints: A, B, C tied in points (diffs=0) AND cyclical "ahead" relation
            # Since total races = 7, 'ahead' means winning at least 4 times
            if dab == 0 and dbc == 0 and wab > 3 and wbc > 3 and wca > 3:
                valid_regattas += count

        # Multiply by multinomial coefficient for all permutations of the 7 races
        perm_coeff = factorial(7)
        for count in d_dist:
            perm_coeff //= factorial(count)
        return valid_regattas * perm_coeff

    total_weighted_sum = 0
    # Iterate over all possible distributions of D's ranks (summing to 7 races, each rank used >= once)
    for d_dist in itertools.product(range(1, 5), repeat=4):
        if sum(d_dist) == 7:
            score_D = 4*d_dist[0] + 3*d_dist[1] + 2*d_dist[2] + 1*d_dist[3]
            # Total points across 7 races for all boats = 7 * (4+3+2+1) = 70
            remaining_points = 70 - score_D
            # A, B, and C must tie
            if remaining_points % 3 == 0:
                score_X = remaining_points // 3
                # D must be the winner (highest score)
                if score_D > score_X:
                    n_regattas = count_regattas_for_d_dist(d_dist)
                    total_weighted_sum += n_regattas * score_D

    return total_weighted_sum

print(solve())
