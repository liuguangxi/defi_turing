def solve():
    # The modulus specified in the problem
    mod = 288
    # dp[i] stores the smallest integer in S such that the integer % 288 == i
    dp = [float('inf')] * mod

    # S is the set of sums of distinct cubes of odd integers.
    # We iterate through odd integers (1, 3, 5, ...) and their cubes.
    # Because cubes grow cubically and we want to find the minimum sum for each residue,
    # we only need to consider a finite number of cubes.
    # Once the current cube is larger than the maximum value in dp, no further improvements can be made.
    for k in range(1, 100):
        x = 2 * k - 1
        cube = x**3

        # Copy the current best results to update for the new cube
        new_dp = list(dp)

        # Case 1: The cube itself represents a sum of a single distinct odd cube
        if cube < new_dp[cube % mod]:
            new_dp[cube % mod] = cube

        # Case 2: Add the new cube to existing sums of distinct odd cubes
        for r in range(mod):
            if dp[r] != float('inf'):
                new_r = (r + cube) % mod
                new_val = dp[r] + cube
                if new_val < new_dp[new_r]:
                    new_dp[new_r] = new_val

        # If no values changed and we've processed enough cubes, we can stop early.
        if dp == new_dp and k > 40:
            break

        dp = new_dp

    # The problem asks for the sum of all s_i for i from 0 to 287.
    # In our dp array, dp[i] corresponds exactly to s_i.
    return sum(dp)

print(solve())
