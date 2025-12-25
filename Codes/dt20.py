def solve():
    # Function to calculate blow count after defeating one 3-headed hydra
    # Starting from blow count t, one blow turns it into (t+2) 2-headed hydras.
    # Defeating k 2-headed hydras results in blow count: 2^k * (t + 3) - 3.
    def defeat_3_headed(t):
        return 2**(t + 2) * (t + 4) - 3

    # Starting with 1 four-headed hydra at t=0:
    # Blow 1: It turns into (0 + 2) = 2 three-headed hydras.
    # Now we defeat two 3-headed hydras starting at t=1.
    step1 = defeat_3_headed(1)  # Time after defeating the first 3-headed hydra
    step2 = defeat_3_headed(step1) # Time after defeating the second 3-headed hydra

    return step2

print(solve())
